// Generated by gencpp from file vector_map_msgs/RoadMark.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_MSGS_MESSAGE_ROADMARK_H
#define VECTOR_MAP_MSGS_MESSAGE_ROADMARK_H


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
struct RoadMark_
{
  typedef RoadMark_<ContainerAllocator> Type;

  RoadMark_()
    : id(0)
    , aid(0)
    , type(0)
    , linkid(0)  {
    }
  RoadMark_(const ContainerAllocator& _alloc)
    : id(0)
    , aid(0)
    , type(0)
    , linkid(0)  {
  (void)_alloc;
    }



   typedef int32_t _id_type;
  _id_type id;

   typedef int32_t _aid_type;
  _aid_type aid;

   typedef int32_t _type_type;
  _type_type type;

   typedef int32_t _linkid_type;
  _linkid_type linkid;



  enum {
    MARK = 1u,
    ARROW = 2u,
    CHARACTER = 3u,
    SIGN = 4u,
  };


  typedef boost::shared_ptr< ::vector_map_msgs::RoadMark_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vector_map_msgs::RoadMark_<ContainerAllocator> const> ConstPtr;

}; // struct RoadMark_

typedef ::vector_map_msgs::RoadMark_<std::allocator<void> > RoadMark;

typedef boost::shared_ptr< ::vector_map_msgs::RoadMark > RoadMarkPtr;
typedef boost::shared_ptr< ::vector_map_msgs::RoadMark const> RoadMarkConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vector_map_msgs::RoadMark_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vector_map_msgs::RoadMark_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vector_map_msgs::RoadMark_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::RoadMark_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::RoadMark_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
{
  static const char* value()
  {
    return "da20a5104558c92bc92163ecb67c4d2a";
  }

  static const char* value(const ::vector_map_msgs::RoadMark_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xda20a5104558c92bULL;
  static const uint64_t static_value2 = 0xc92163ecb67c4d2aULL;
};

template<class ContainerAllocator>
struct DataType< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vector_map_msgs/RoadMark";
  }

  static const char* value(const ::vector_map_msgs::RoadMark_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# type\n\
uint8 MARK=1\n\
uint8 ARROW=2\n\
uint8 CHARACTER=3\n\
uint8 SIGN=4\n\
\n\
# Ver 1.00\n\
int32 id\n\
int32 aid\n\
int32 type # differ from specification\n\
int32 linkid\n\
";
  }

  static const char* value(const ::vector_map_msgs::RoadMark_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.aid);
      stream.next(m.type);
      stream.next(m.linkid);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RoadMark_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vector_map_msgs::RoadMark_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vector_map_msgs::RoadMark_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "aid: ";
    Printer<int32_t>::stream(s, indent + "  ", v.aid);
    s << indent << "type: ";
    Printer<int32_t>::stream(s, indent + "  ", v.type);
    s << indent << "linkid: ";
    Printer<int32_t>::stream(s, indent + "  ", v.linkid);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VECTOR_MAP_MSGS_MESSAGE_ROADMARK_H
