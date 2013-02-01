#include <ros/ros.h>
#include <std_msgs/String.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <rosgraph_msgs/Clock.h>


class Keyboard
{

  //Ros objects
  ros::NodeHandle nh_;

  ros::Publisher vmd_vel_publisher_;

public:
  Keyboard(ros::NodeHandle& nh) :
    nh_(nh),
    vmd_vel_publisher_(nh_.advertise<geometry_msgs::Twist> ("/cmd_vel", 1))
  {
    ROS_INFO("Started Keyboard Node");
  }

  void run(int argc, char** argv)
  {
    // Initialize ROS
    ros::Rate r(10);

    while (nh_.ok())
    {
      char kp;
      //std::cin >> kp;
      kp = std::getch();
      std::cout << (int)kp << std::endl;
      ros::spinOnce();
    }
  }

};

int main(int argc, char** argv)
{
  ros::init(argc, argv, "smr_keyboard_node");
  ros::NodeHandle nh;
  Keyboard component(nh);

  component.run(argc, argv);
  return 0;
}

