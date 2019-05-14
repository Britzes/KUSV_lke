// Generated by gencpp from file vector_map_server/GetRailCrossing.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_SERVER_MESSAGE_GETRAILCROSSING_H
#define VECTOR_MAP_SERVER_MESSAGE_GETRAILCROSSING_H

#include <ros/service_traits.h>


#include <vector_map_server/GetRailCrossingRequest.h>
#include <vector_map_server/GetRailCrossingResponse.h>


namespace vector_map_server
{

struct GetRailCrossing
{

typedef GetRailCrossingRequest Request;
typedef GetRailCrossingResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetRailCrossing
} // namespace vector_map_server


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::vector_map_server::GetRailCrossing > {
  static const char* value()
  {
    return "76f69b076c0ee1fce929a2da3f0574a4";
  }

  static const char* value(const ::vector_map_server::GetRailCrossing&) { return value(); }
};

template<>
struct DataType< ::vector_map_server::GetRailCrossing > {
  static const char* value()
  {
    return "vector_map_server/GetRailCrossing";
  }

  static const char* value(const ::vector_map_server::GetRailCrossing&) { return value(); }
};


// service_traits::MD5Sum< ::vector_map_server::GetRailCrossingRequest> should match 
// service_traits::MD5Sum< ::vector_map_server::GetRailCrossing > 
template<>
struct MD5Sum< ::vector_map_server::GetRailCrossingRequest>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetRailCrossing >::value();
  }
  static const char* value(const ::vector_map_server::GetRailCrossingRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetRailCrossingRequest> should match 
// service_traits::DataType< ::vector_map_server::GetRailCrossing > 
template<>
struct DataType< ::vector_map_server::GetRailCrossingRequest>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetRailCrossing >::value();
  }
  static const char* value(const ::vector_map_server::GetRailCrossingRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::vector_map_server::GetRailCrossingResponse> should match 
// service_traits::MD5Sum< ::vector_map_server::GetRailCrossing > 
template<>
struct MD5Sum< ::vector_map_server::GetRailCrossingResponse>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetRailCrossing >::value();
  }
  static const char* value(const ::vector_map_server::GetRailCrossingResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetRailCrossingResponse> should match 
// service_traits::DataType< ::vector_map_server::GetRailCrossing > 
template<>
struct DataType< ::vector_map_server::GetRailCrossingResponse>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetRailCrossing >::value();
  }
  static const char* value(const ::vector_map_server::GetRailCrossingResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // VECTOR_MAP_SERVER_MESSAGE_GETRAILCROSSING_H
