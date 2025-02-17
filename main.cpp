#include <iostream>
#include <vector>
#include <string>
#include "header.hpp"
using namespace std; 

class Player {
  public:
  int health;
  int score;
  int level; 

  //empty intialized constructor
  Player () {
    health = 100; 
    score = 0;
    level = 1; 
  }

void PrintPlayer(Player p) {
  if (p.health <= 0) {
    cout << "This player is dead. They died on level " << p.level;
    cout << " with a score of " << p.score << "." << endl;
  }
  else {
    cout << "This player has " << p.health << " health, a score of " << p.score;
    cout << ", and is on level " << p.level << "." << endl;
  }
}

void ChangeHealth(Player p, int amount) {
  p.health += amount;
  cout << "New health = " << p.health << endl;
}

}; 

//create an class called meals with arrays of drinks appetizers main course desert

class Meal 
{
  private: 
    vector <string> drinks;
    vector <string> appetizers;
    vector <string> main_course;
    vector <string> desert;
  
  public: 
  //add a function to add a meal to the array. 

  void Add_Drinks (string drink) 
  {
    drinks.push_back(drink); 
  }

  //print the array 
  void Print_Drinks ()
  {
    for (auto i : drinks)
    {
      cout << i << endl; 
    }
  }

  void Add_App (string app) 
  {
    appetizers.push_back(app); 
  }


}; 

 
//function to calculate area
template <class data_type> 
data_type area_rect(data_type a, data_type b) 
{
	data_type result = a*b;
	return result; 
}

int main() 
{


int x = area_rect<int>(3, 1);  
float y = area_rect<float>(3.667, 1.5); 
double z = area_rect<double>(3.667, 1.5); 
cout << x << ", " << y << ", " << z <<endl; 

 return 0;
  
}