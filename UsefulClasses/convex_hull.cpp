#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <iostream>

struct Vector {
  int dx;
  int dy;
};

int cross_product(const Vector& a, const Vector& b) {
  return a.dx * b.dy - a.dy * b.dx;
}

struct Point {
  int x;
  int y;

  Vector operator-(const Point& other) {
    return Vector{.dx = x - other.x, .dy = y - other.y};
  }

  bool operator<(const Point& other) const {
    if (x != other.x) {
      return x < other.x;
    }
    return y < other.y;
  }

};

class ConvexHull {
 private:
  // points[x][y]=c means we have c points at (x,y)
  std::map<int, std::map<int, int>> points_;

  // upper_curve_history_[(x,y)]={(a,b), (c,d)} means
  // On the current convex hull, (x,y) next point is (c,d)
  // But if (c,d) is removed, (a,b) is the next choice.
  std::map<Point, std::vector<Point>> upper_curve_history_;
  std::set<Point> upper_curve_;

  std::map<Point, std::vector<Point>> lower_curve_history_;
  std::set<Point> lower_curve_;

 public:
  ConvexHull(const std::vector<Point> points) {
    for (const Point& point : points) {
      this->points_[point.x][point.y]++;
    }

    if (points_.size() == 0) {
      return;
    }

    calculate_upper_curve();
    calculate_lower_curve();
  }

  void calculate_upper_curve() {
    for (const auto& [x, y_to_count] : points_) {
      Point p = Point{.x = x, .y = y_to_count.rbegin()->first};

      while (true) {
        std::set<Point>::reverse_iterator last_it = upper_curve_.rbegin();
        if (last_it == upper_curve_.rend()) {
          break;
        }        
        Point last_p = *last_it;

        last_it++;
        if (last_it == upper_curve_.rend()) {
          break;
        }
        Point last_second_p = *last_it;

        if (cross_product(last_p - last_second_p, p - last_p ) >=0) {
          upper_curve_.erase(last_p);
        }
        else {
          break;
        }
      }

      if (!upper_curve_.empty()) {
        upper_curve_history_[*upper_curve_.rbegin()].push_back(p);
      }
      upper_curve_.insert(p);
    }
  }

  void calculate_lower_curve() {
    for (const auto& [x, y_to_count] : points_) {
      Point p = Point{.x = x, .y = y_to_count.begin()->first};

      while (true) {
        std::set<Point>::reverse_iterator last_it = lower_curve_.rbegin();
        if (last_it == lower_curve_.rend()) {
          break;
        }        
        Point last_p = *last_it;

        last_it++;
        if (last_it == lower_curve_.rend()) {
          break;
        }
        Point last_second_p = *last_it;

        if (cross_product(last_p - last_second_p, p - last_p ) <=0) {
          lower_curve_.erase(last_p);
        }
        else {
          break;
        }
      }

      if (!lower_curve_.empty()) {
        lower_curve_history_[*lower_curve_.rbegin()].push_back(p);
      }
      lower_curve_.insert(p);
    }
  }

  std::vector<Point> full_hull() {
    std::vector<Point> result;

    for (const Point& p : upper_curve_) {
      result.push_back(p);
    }

    auto lower_it = lower_curve_.rbegin();
    if (lower_curve_.rbegin()->y == upper_curve_.rbegin()->y) {
        lower_it++;
    }
    for (; lower_it != lower_curve_.rend(); lower_it++) {
        result.push_back(*lower_it);
    }

    if (lower_curve_.begin()->y != upper_curve_.begin()->y) {
        result.push_back(*upper_curve_.begin());
    }
    return result;
  }

  void fix_upper_curve(const Point& starting_point, int x_stop_line) {
    // Follow history
    Point p = starting_point;
    do {
      while (!upper_curve_history_[p].empty()) {
        const Point& next_candidate = upper_curve_history_[p].back();
        if (!points_exist(next_candidate)) {
          upper_curve_history_[p].pop_back();
          continue;
        }
        else {
          break;
        }
      }

      if (!upper_curve_history_[p].empty()) {
        p = upper_curve_history_[p].back();
        if (p.x <= x_stop_line) {
          upper_curve_.insert(p);
          continue;
        }
      }
      else{
        break;
      }
    }
    while(true);

    if (p.x >= x_stop_line) {
      return;
    }

    for (auto it = points_.upper_bound(p.x); it != points_.end(); it++) {
      Point p = Point{.x = it->first, .y = it->second.rbegin()->first};

      while (true) {
        std::set<Point>::iterator last_it = upper_curve_.lower_bound(p);
        if (last_it == upper_curve_.begin()) {
          break;
        }
        last_it--;
        Point last_p = *last_it;
        
        if (last_it == upper_curve_.begin()) {
          break;
        }
        last_it--;
        Point last_second_p = *last_it;

        if (cross_product(last_p - last_second_p, p - last_p ) >=0) {
          upper_curve_.erase(last_p);
        }
        else {
          break;
        }
      }

      if (upper_curve_.lower_bound(p) != upper_curve_.begin()) {
        upper_curve_history_[*std::next(upper_curve_.lower_bound(p), -1)].push_back(p);
      }
      upper_curve_.insert(p);
    }     
  }

  void fix_lower_curve(const Point& starting_point, int x_stop_line) {
    // Follow history
    Point p = starting_point;
    do {
      while (!lower_curve_history_[p].empty()) {
        const Point& next_candidate = lower_curve_history_[p].back();
        if (!points_exist(next_candidate)) {
          lower_curve_history_[p].pop_back();
          continue;
        }
        else {
          break;
        }
      }

      if (!lower_curve_history_[p].empty()) {
        p = lower_curve_history_[p].back();
        if (p.x <= x_stop_line) {
          lower_curve_.insert(p);
          continue;
        }
      }
      else{
        break;
      }
    }
    while(true);

    if (p.x >= x_stop_line) {
      return;
    }

    for (auto it = points_.upper_bound(p.x); it != points_.end(); it++) {
      Point p = Point{.x = it->first, .y = it->second.begin()->first};

      while (true) {
        std::set<Point>::iterator last_it = lower_curve_.lower_bound(p);
        if (last_it == lower_curve_.begin()) {
          break;
        }
        last_it--;
        Point last_p = *last_it;
        
        if (last_it == lower_curve_.begin()) {
          break;
        }
        last_it--;
        Point last_second_p = *last_it;

        if (cross_product(last_p - last_second_p, p - last_p ) <=0) {
          lower_curve_.erase(last_p);
        }
        else {
          break;
        }
      }

      if (lower_curve_.lower_bound(p) != lower_curve_.begin()) {
        lower_curve_history_[*std::next(lower_curve_.lower_bound(p), -1)].push_back(p);
      }
      lower_curve_.insert(p);
    }     
  }

  void fix_upper_curve_begin(int x_stop_line) {
    Point p = Point{
      .x = points_.begin()->first,
      .y = points_.begin()->second.rbegin()->first
    };

    upper_curve_.insert(p);
    fix_upper_curve(p, x_stop_line);
  }

  void fix_lower_curve_begin(int x_stop_line) {
    Point p = Point{
      .x = points_.begin()->first,
      .y = points_.begin()->second.begin()->first
    };

    lower_curve_.insert(p);
    fix_lower_curve(p, x_stop_line);
  }

  void erase_point_from_upper_curve(const Point& p) {
    std::set<Point>::iterator it = upper_curve_.lower_bound(p);

    if (it == upper_curve_.begin()) {
      int x_stop_line = it->x;
      it++;
      if (it != upper_curve_.end())  {
        x_stop_line = it->x;
      }

      upper_curve_.erase(p);
      fix_upper_curve_begin(x_stop_line);
    }
    else {
      std::set<Point>::iterator prev = std::next(it, -1);
      
      int x_stop_line = it->x;
      it++;
      if (it != upper_curve_.end())  {
        x_stop_line = it->x;
      }

      upper_curve_.erase(p);
      fix_upper_curve(*prev, x_stop_line);
    }
  }

  void erase_point_from_lower_curve(const Point& p) {
    std::set<Point>::iterator it = lower_curve_.lower_bound(p);

    if (it == lower_curve_.begin()) {
      int x_stop_line = it->x;
      it++;
      if (it != lower_curve_.end())  {
        x_stop_line = it->x;
      }

      lower_curve_.erase(p);
      fix_lower_curve_begin(x_stop_line);
    }
    else {
      std::set<Point>::iterator prev = std::next(it, -1);
      
      int x_stop_line = it->x;
      it++;
      if (it != lower_curve_.end())  {
        x_stop_line = it->x;
      }

      lower_curve_.erase(p);
      fix_lower_curve(*prev, x_stop_line);
    }
  }

  void remove_point(const Point& p) {
    if (!points_exist(p)) {
      return;
    }

    points_[p.x][p.y]--;
    bool points_gone = false;
    if (points_[p.x][p.y] <=0) {
      points_[p.x].erase(p.y);
      points_gone = true;
    }

    if (points_[p.x].size() == 0) {
      points_.erase(p.x);
    }

    if (points_gone && upper_curve_.count(p) > 0) {
      erase_point_from_upper_curve(p);
    }

    if (points_gone && lower_curve_.count(p) > 0) {
      erase_point_from_lower_curve(p);
    }
  }

  bool points_exist (const Point& p) {
    if (points_.count(p.x) == 0) {
      return false;
    }

    if (points_.at(p.x).count(p.y) == 0 || points_.at(p.x).at(p.y) == 0) {
      return false;
    }

    return true;
  }

  void debug_output_upper_history() {
    for (const auto& [p, history] : upper_curve_history_) {
      std::cout << p.x <<"," << p.y<<"  ";

      for (const Point& q: history) {
        std::cout << "("<< q.x <<","<<q.y <<")";
      }
      std::cout << std::endl;
    }
  }
};

int main() {
    ConvexHull myhull ({
        {1,4}, {1,3}, {0,0}, {2,1},{0, -1}, {2,2}, {1,1}, {3,6}
    });

    std::vector<Point> convex_hull = myhull.full_hull();

    for (int i = 0; i < convex_hull.size(); i++) {
        std::cout << convex_hull[i].x << "," << convex_hull[i].y << std::endl;
    }
    std::cout << std::endl;
    myhull.debug_output_upper_history();

    myhull.remove_point(Point{0,0});
    myhull.remove_point(Point{0,-1});
    myhull.remove_point(Point{2,1});
    myhull.remove_point(Point{1,4});
    convex_hull = myhull.full_hull();
    for (int i = 0; i < convex_hull.size(); i++) {
        std::cout << convex_hull[i].x << "," << convex_hull[i].y << std::endl;
    }
    std::cout << std::endl;

    myhull.debug_output_upper_history();
}