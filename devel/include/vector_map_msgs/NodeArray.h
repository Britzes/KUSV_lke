// Generated by gencpp from file vector_map_msgs/NodeArray.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_MSGS_MESSAGE_NODEARRAY_H
#define VECTOR_MAP_MSGS_MESSAGE_NODEARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <vector_map_msgs/Node.h>

namespace vector_map_msgs
{
template <class ContainerAllocator>
struct NodeArray_
{
  typedef NodeArray_<ContainerAllocator> Type;

  NodeArray_()
    : header()
    , data()  {
    }
  NodeArray_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , data(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::vector_map_msgs::Node_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::vector_map_msgs::Node_<ContainerAllocator> >::other >  _data_type;
  _data_type data;





  typedef boost::shared_ptr< ::vector_map_msgs::NodeArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vector_map_msgs::NodeArray_<ContainerAllocator> const> ConstPtr;

}; // struct NodeArray_

typedef ::vector_map_msgs::NodeArray_<std::allocator<void> > NodeArray;

typedef boost::shared_ptr< ::vector_map_msgs::NodeArray > NodeArrayPtr;
typedef boost::shared_ptr< ::vector_map_msgs::NodeArray const> NodeArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vector_map_msgs::NodeArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vector_map_msgs::NodeArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vector_map_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'vector_map_msgs': ['/home/lke/kusv_ke/kusv_ros/src/data/packages/vector_map_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vector_map_msgs::NodeArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vector_map_msgs::NodeArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vector_map_msgs::NodeArray_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "77073c90205106235cda21d84d1bdd61";
  }

  static const char* value(const ::vector_map_msgs::NodeArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x77073c9020510623ULL;
  static const uint64_t static_value2 = 0x5cda21d84d1bdd61ULL;
};

template<class ContainerAllocator>
struct DataType< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vector_map_msgs/NodeArray";
  }

  static const char* value(const ::vector_map_msgs::NodeArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
Node[] data\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: vector_map_msgs/Node\n\
# Ver 1.00\n\
int32 nid\n\
int32 pid\n\
";
  }

  static const char* value(const ::vector_map_msgs::NodeArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.data);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct NodeArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vector_map_msgs::NodeArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vector_map_msgs::NodeArray_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "data[]" << std::endl;
    for (size_t i = 0; i < v.data.size(); ++i)
    {
      s << indent << "  data[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::vector_map_msgs::Node_<ContainerAllocator> >::stream(s, indent + "    ", v.data[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // VECTOR_MAP_MSGS_MESSAGE_NODEARRAY_H
