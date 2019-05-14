// Generated by gencpp from file vector_map_msgs/RoadPole.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_MSGS_MESSAGE_ROADPOLE_H
#define VECTOR_MAP_MSGS_MESSAGE_ROADPOLE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace vector_map_msgs
{
template <class ContainerAllocator>
struct RoadPole_
{
  typedef RoadPole_<ContainerAllocator> Type;

  RoadPole_()
    : id(0)
    , plid(0)
    , linkid(0)  {
    }
  RoadPole_(const ContainerAllocator& _alloc)
    : id(0)
    , plid(0)
    , linkid(0)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef int32_t _plid_type;
  _plid_type plid;

   typedef int32_t _linkid_type;
  _linkid_type linkid;





  typedef boost::shared_ptr< ::vector_map_msgs::RoadPole_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vector_map_msgs::RoadPole_<ContainerAllocator> const> ConstPtr;

}; // struct RoadPole_

typedef ::vector_map_msgs::RoadPole_<std::allocator<void> > RoadPole;

typedef boost::shared_ptr< ::vector_map_msgs::RoadPole > RoadPolePtr;
typedef boost::shared_ptr< ::vector_map_msgs::RoadPole const> RoadPoleConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vector_map_msgs::RoadPole_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vector_map_msgs::RoadPole_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vector_map_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'vector_map_msgs': ['/home/lke/kusv_ke/kusv_ros/src/data/packages/vector_map_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vector_map_msgs::RoadPole_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::RoadPole_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::RoadPole_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4bae6d2155106d4f26850fd9cc39bd6d";
  }

  static const char* value(const ::vector_map_msgs::RoadPole_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4bae6d2155106d4fULL;
  static const uint64_t static_value2 = 0x26850fd9cc39bd6dULL;
};

template<class ContainerAllocator>
struct DataType< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vector_map_msgs/RoadPole";
  }

  static const char* value(const ::vector_map_msgs::RoadPole_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Ver 1.00\n\
int32 id\n\
int32 plid\n\
int32 linkid\n\
";
  }

  static const char* value(const ::vector_map_msgs::RoadPole_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.plid);
      stream.next(m.linkid);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RoadPole_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vector_map_msgs::RoadPole_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vector_map_msgs::RoadPole_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "plid: ";
    Printer<int32_t>::stream(s, indent + "  ", v.plid);
    s << indent << "linkid: ";
    Printer<int32_t>::stream(s, indent + "  ", v.linkid);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VECTOR_MAP_MSGS_MESSAGE_ROADPOLE_H
