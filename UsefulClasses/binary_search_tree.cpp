/**
 * This file provides a class that performs a balanced binary search tree.
 * 
 * The standard cpp tree map lacks the following API:
 *  1. Given int l, return the l-th min element of the tree.
 *  2. Given key k, return the number of elements in the tree that are smaller than k.
 */

#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
#include <cassert>

template<typename K, typename V>
struct Node {
    int id;
    int parent_id = -1;
    int left_id = -1;    
    int right_id = -1;

    K key = K();
    V value = V();

    // Subtree property
    int height = 1;
    int size = 1;

    // Aggregate Stuff
    V aggregate_value = V();
};

// Aggregate function must be commutative and associative.
template<typename V>
using AggregateFunc = V (*) (const V& v1, const V& v2);

template<typename K, typename V>
class BST {
  private:
    std::vector<Node<K, V>> nodes_;
    int root_;

    int create_node_and_attach_to(int parent, const K& key, const V& value);
    void post_insert(int curr);
    
    // rebalance the subtree at curr.
    // Assume: all substrees of curr's children are balanced. 
    void rebalance_on_node(int curr);

    // rotate curr to the position of its parent.
    void rotate(int curr);
    void recalculate_statistics_on_node(int node_id);                                                                                                                                    

    void debug_output_on_node(int depth, int node);
    void debug_validate_on_node(int node);

    AggregateFunc<V> aggregate_func_;
  public:
    BST(AggregateFunc<V> aggregate_func);

    void upsert(const K& key, const V& value);

    bool containsKey(const K& key);

    int size();

    // Get the l-th min element.
    // Throws out of bound exception.
    std::pair<K,V> get(int l);

    // Returns the # of elements in the
    // tree less than `key`.
    int index(const K& key);

    void debug_output();
    void debug_output_recur();
    void debug_validate();

  // The following is for range based loop
  public: 
    class iterator {
      private:
        BST* bst_;
        int node_id_;
      public:
        iterator(BST* bst, int node_id);
        iterator& operator++();
        bool operator!=(const iterator& other);
        std::pair<K,V> operator*();
    };

    iterator begin();
    iterator end();
};

template<typename K, typename V>
BST<K,V>::iterator::iterator(BST<K,V>* bst, int node_id) {
    bst_ = bst;
    node_id_ = node_id;
}

template<typename K, typename V>
BST<K,V>::iterator& BST<K,V>::iterator::operator++() {
    int curr = node_id_;
    if (bst_->nodes_[curr].right_id != -1) {
        curr = bst_->nodes_[curr].right_id;
        while (bst_->nodes_[curr].left_id != -1) {
            curr = bst_->nodes_[curr].left_id;
        }
        node_id_=curr;
        return *this;
    }

    int parent = bst_->nodes_[curr].parent_id;
    while (parent != -1 && bst_->nodes_[parent].right_id == curr) {
        curr = parent;
        parent = bst_->nodes_[curr].parent_id;
    }
    node_id_=parent;

    return *this;
}

template<typename K, typename V>
bool BST<K,V>::iterator::operator!=(const BST<K,V>::iterator& other) {
    return (this->bst_ != other.bst_ || this->node_id_ != other.node_id_);
}

template<typename K, typename V>
std::pair<K,V> BST<K,V>::iterator::operator*() {
    if (node_id_ == -1) {
        throw "Cannot dereference end iterator";
    } 

    return std::make_pair(bst_->nodes_[node_id_].key, bst_->nodes_[node_id_].value);
}

template<typename K, typename V>
BST<K,V>::iterator BST<K,V>::begin() {
    if (root_ == -1) {
        return BST::iterator(this, -1);
    }

    int curr = root_;
    while (nodes_[curr].left_id != -1) {
        curr = nodes_[curr].left_id;
    }
    return BST::iterator(this, curr);
}

template<typename K, typename V>
BST<K,V>::iterator BST<K,V>::end() {
    return BST::iterator(this, -1);
}

template<typename K, typename V>
BST<K,V>::BST(AggregateFunc<V> aggregate_func) {
    root_=-1;
    aggregate_func_ = aggregate_func;
}

template<typename K, typename V>
int BST<K,V>::size() {
    return nodes_.size();
}

template<typename K, typename V>
bool BST<K,V>::containsKey(const K& key) {
    int curr = root_;    
    while (curr != -1) {
        if (key == nodes_[curr].key) {
            return true;
        }
        if (key < nodes_[curr].key) {            
            curr = nodes_[curr].left_id;
        } else if (key > nodes_[curr].key) {            
            curr = nodes_[curr].right_id;
        }
    }
    return false;
}

template<typename K, typename V>
std::pair<K, V> BST<K,V>::get(int index) {
    if (index<0 || index >= size()) {
        throw "index out of bound";
    }

    int curr = root_;
    while (true) {
        int left_id = nodes_[curr].left_id;
        int left_size = (left_id >= 0) ? nodes_[left_id].size : 0;
        if (index == left_size) {
            return std::make_pair(nodes_[curr].key, nodes_[curr].value);
        }
        else if (index < left_size) {
            curr = left_id;
        }
        else if (index > left_size) {
            index -= left_size + 1;
            curr = nodes_[curr].right_id;
        }
    }

    throw "Broken state to get by index";
}

template<typename K, typename V>
int BST<K,V>::index(const K& key) {
    int result = 0;

    int curr = root_;
    while (curr != -1) {
        K curr_key = nodes_[curr].key;

        int left_id = nodes_[curr].left_id;
        int left_size = (left_id >= 0) ? nodes_[left_id].size : 0;

        if (key <= curr_key) {
            curr = left_id;
        }
        else if (key > curr_key) {
            result += left_size + 1;
            curr = nodes_[curr].right_id;
        }
    }
    return result;
}

template<typename K, typename V>
void BST<K,V>::upsert(const K& key, const V& value) {
    if (root_==-1) {
        root_=0;
        nodes_.push_back(
            Node<K,V>{
              .id=root_,
              .key=key,
              .value=value,
              .aggregate_value=value
            }
        );
        return;
    }

    int curr = root_;
    int curr_parent = -1;
    while (curr != -1) {
        if (key == nodes_[curr].key) {
            nodes_[curr].value = value;
            post_insert(curr);
            return;
        }
        if (key < nodes_[curr].key) {
            curr_parent = curr;
            curr = nodes_[curr].left_id;
        } else if (key > nodes_[curr].key) {
            curr_parent = curr;
            curr = nodes_[curr].right_id;
        }
    }

    // To here curr == -1, we need to create a node
    curr = create_node_and_attach_to(curr_parent, key, value);
    post_insert(curr);
    return;
}

/**
 * Note this function will break the statistics.
 */
template<typename K, typename V>
int BST<K,V>::create_node_and_attach_to(int parent, const K& key, const V& value) {
    int curr = nodes_.size();
    nodes_.push_back(
        Node<K,V>{
            .id = curr,
            .parent_id = parent,
            .key=key,
            .value=value,
            .aggregate_value=value
        }
    );
    if (key < nodes_[parent].key){
        nodes_[parent].left_id = curr;
    }
    else {
        nodes_[parent].right_id = curr;
    }

    return curr;
}

template<typename K, typename V>
void BST<K,V>::post_insert(int node_id) {
    // The input node_id is at the bottom, so 
    // only consider that node as a subtree, the statistics
    // is well maintained, and the tree is balanced.
    int curr = node_id;
    while (curr != -1) { 
        recalculate_statistics_on_node(curr);

        // rebalance the subtree at curr.
        // Assuming all the subtree of curr are rebalanced.
        rebalance_on_node(curr);

        curr = nodes_[curr].parent_id;       
    }
}

template<typename K, typename V>
void BST<K,V>::rotate(int node_id) {
    if (node_id == root_) {
        return;
    }

    int parent = nodes_[node_id].parent_id;
    int grand_parent = nodes_[parent].parent_id;

    int left = nodes_[node_id].left_id;
    int right = nodes_[node_id].right_id;
    
    bool iam_left = (node_id == nodes_[parent].left_id);

    if (iam_left) {
         // Parent take over my right kid as its left kid.
        nodes_[parent].left_id = right;
        nodes_[right].parent_id = parent;

        // Make parent become my right kid
        nodes_[node_id].right_id = parent;
        nodes_[parent].parent_id = node_id;       
    }
    else {        
        // Parent take over my left kid as its right kid.
        nodes_[parent].right_id = left;
        nodes_[left].parent_id = parent;

        // Make parent become my left kid
        nodes_[node_id].left_id = parent;
        nodes_[parent].parent_id = node_id;       
    }

    // I become my grand parent's kid.
    nodes_[node_id].parent_id = grand_parent;

    if (grand_parent == -1) {
        root_ = node_id;
    }
    else {
        if (nodes_[grand_parent].left_id == parent) {
            nodes_[grand_parent].left_id = node_id;
        } else {
            assert(nodes_[grand_parent].right_id == parent);
            nodes_[grand_parent].right_id = node_id;            
        }
    }

    recalculate_statistics_on_node(parent);
    recalculate_statistics_on_node(node_id);
    recalculate_statistics_on_node(grand_parent);
}

template<typename K, typename V>
void BST<K,V>::recalculate_statistics_on_node(int node_id) {
    if (node_id == -1) {
        return;
    }
    int curr = node_id;

    int left_id = nodes_[curr].left_id;
    int right_id = nodes_[curr].right_id;
    int left_size = left_id >=0 ? nodes_[left_id].size : 0;
    int right_size = right_id >=0 ? nodes_[right_id].size : 0;
    int left_height = left_id >=0 ? nodes_[left_id].height : 0;
    int right_height = right_id >=0 ? nodes_[right_id].height : 0;
    nodes_[curr].size = 1 + left_size + right_size;
    nodes_[curr].height = 1 + std::max(left_height, right_height);

    // Recalculate the aggregate value
    nodes_[curr].aggregate_value = nodes_[curr].value;
    if (left_id >= 0) {
        nodes_[curr].aggregate_value = aggregate_func_(
            nodes_[curr].aggregate_value,
            nodes_[left_id].aggregate_value
        );
    }
    if (right_id >= 0) {
        nodes_[curr].aggregate_value = aggregate_func_(
            nodes_[curr].aggregate_value,
            nodes_[right_id].aggregate_value
        );
    }

}

template<typename K, typename V>
void BST<K,V>::rebalance_on_node(int node_id) {
    int left_id = nodes_[node_id].left_id;
    int right_id = nodes_[node_id].right_id;
    int left_height = left_id >=0 ? nodes_[left_id].height : 0;
    int right_height = right_id >=0 ? nodes_[right_id].height : 0;

    // AVL condition already satisfied.
    if (std::abs(left_height - right_height) <= 1) {
        return;
    }

    if (left_height == right_height + 2) {
        int left_left_id = nodes_[left_id].left_id;
        int left_right_id = nodes_[left_id].right_id;
        int left_left_height = left_left_id >=0 ? nodes_[left_left_id].height : 0;
        int left_right_height = left_right_id >=0 ? nodes_[left_right_id].height : 0;

        if (left_left_height == right_height + 1 || left_right_height == right_height) {
            rotate(left_id);
            return;
        }
        else {
            // left_left_height == right_height && left_right_height == right_height+1
            rotate(left_right_id);
            rotate(left_right_id);
            return;
        }
    }
    else if (right_height == left_height + 2) {
        int right_left_id = nodes_[right_id].left_id;
        int right_right_id = nodes_[right_id].right_id;
        int right_left_height = right_left_id >=0 ? nodes_[right_left_id].height : 0;
        int right_right_height = right_right_id >=0 ? nodes_[right_right_id].height : 0;

        if (right_right_height == left_height + 1 || right_left_height == left_height) {
            rotate(right_id);
            return;
        }
        else {
            // right_right_height == left_height && right_left_height == left_height+1
            rotate(right_left_id);
            rotate(right_left_id);
            return;
        }
    }
    else {
        throw "Rebalance failed for the left right height diff not valid";
    }
}

template<typename K, typename V>
void BST<K,V>::debug_output() {
    for (int i = 0; i < nodes_.size(); i++) {
        std::cout << nodes_[i].id 
            << " parent=" << nodes_[i].parent_id
            << " left=" << nodes_[i].left_id
            << " right=" << nodes_[i].right_id
            << " key=" << nodes_[i].key
            << " value=" << nodes_[i].value
            << " height=" << nodes_[i].height
            << " size=" << nodes_[i].size
            << std::endl;
    }
}

template<typename K, typename V>
void BST<K,V>::debug_validate_on_node(int node_id) {
    if (node_id == -1) {
        return;
    }

    int left_id = nodes_[node_id].left_id;
    int right_id = nodes_[node_id].right_id;
    int left_size = left_id >=0 ? nodes_[left_id].size : 0;
    int right_size = right_id >=0 ? nodes_[right_id].size : 0;
    int left_height = left_id >=0 ? nodes_[left_id].height : 0;
    int right_height = right_id >=0 ? nodes_[right_id].height : 0;
    
    if (nodes_[node_id].size != 1 + left_size + right_size) {
        std::cout << "Size constraint violated at "<< node_id << std::endl;
    }

    if (nodes_[node_id].height != 1 + std::max(left_height, right_height)) {
        std::cout << "Size constraint violated at "<< node_id << std::endl;
    }

    if (left_id != -1 && nodes_[left_id].parent_id != node_id) {
        std::cout << "Left Link broken at " << node_id << std::endl;
    }

    if (right_id != -1 && nodes_[right_id].parent_id != node_id) {        
        std::cout << "Right Link broken at " << node_id << std::endl;
    }

    if (std::abs(left_height-right_height) >1) {
        std::cout << "AVL Condition Violated at " << node_id << std::endl;
    }

    if (left_id != -1 && nodes_[left_id].key > nodes_[node_id].key) {
        std::cout << "Value smaller than left at " << node_id << std::endl;
    }

    if (right_id != -1 && nodes_[right_id].key < nodes_[node_id].key) {
        std::cout << "Value bigger than right at " << node_id << std::endl;
    }

    debug_validate_on_node(left_id);
    debug_validate_on_node(right_id);
}

template<typename K, typename V>
void BST<K,V>::debug_validate() {
    debug_validate_on_node(root_);
}

template<typename K, typename V>
void BST<K,V>::debug_output_recur() {
    debug_output_on_node(0, root_);
    std::cout << std::endl;
}

template<typename K, typename V>
void BST<K,V>::debug_output_on_node(int depth, int node_id) {    
    for (int i = 0; i < depth; i++) {
        std::cout << " ";
    }
    if (node_id == -1) {
        std::cout << -1 <<std::endl;
        return;
    }
    std::cout << nodes_[node_id].key << " " << nodes_[node_id].value << " agg=" << nodes_[node_id].aggregate_value << std::endl;
    debug_output_on_node(depth+1, nodes_[node_id].left_id);
    debug_output_on_node(depth+1, nodes_[node_id].right_id);
}

int main() {
    BST<int, int> bst(
        [](const int& v1, const int& v2){
            return v1+v2;
        }
    );
    for (int i = 10; i >=0; i--) {
        bst.upsert(i+i, i);
    }

    bst.debug_validate();
       
    for (const auto& [k,v] : bst) {
        std::cout << k <<" ";
    }
    std::cout << std::endl;
    
    bst.debug_output_recur();
}