// Generated by gencpp from file vector_map_server/GetGutter.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_SERVER_MESSAGE_GETGUTTER_H
#define VECTOR_MAP_SERVER_MESSAGE_GETGUTTER_H

#include <ros/service_traits.h>


#include <vector_map_server/GetGutterRequest.h>
#include <vector_map_server/GetGutterResponse.h>


namespace vector_map_server
{

struct GetGutter
{

typedef GetGutterRequest Request;
typedef GetGutterResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetGutter
} // namespace vector_map_server


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::vector_map_server::GetGutter > {
  static const char* value()
  {
    return "f1bbd06d1252dc2b480df9448d5fffc0";
  }

  static const char* value(const ::vector_map_server::GetGutter&) { return value(); }
};

template<>
struct DataType< ::vector_map_server::GetGutter > {
  static const char* value()
  {
    return "vector_map_server/GetGutter";
  }

  static const char* value(const ::vector_map_server::GetGutter&) { return value(); }
};


// service_traits::MD5Sum< ::vector_map_server::GetGutterRequest> should match 
// service_traits::MD5Sum< ::vector_map_server::GetGutter > 
template<>
struct MD5Sum< ::vector_map_server::GetGutterRequest>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetGutter >::value();
  }
  static const char* value(const ::vector_map_server::GetGutterRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetGutterRequest> should match 
// service_traits::DataType< ::vector_map_server::GetGutter > 
template<>
struct DataType< ::vector_map_server::GetGutterRequest>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetGutter >::value();
  }
  static const char* value(const ::vector_map_server::GetGutterRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::vector_map_server::GetGutterResponse> should match 
// service_traits::MD5Sum< ::vector_map_server::GetGutter > 
template<>
struct MD5Sum< ::vector_map_server::GetGutterResponse>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetGutter >::value();
  }
  static const char* value(const ::vector_map_server::GetGutterResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetGutterResponse> should match 
// service_traits::DataType< ::vector_map_server::GetGutter > 
template<>
struct DataType< ::vector_map_server::GetGutterResponse>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetGutter >::value();
  }
  static const char* value(const ::vector_map_server::GetGutterResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // VECTOR_MAP_SERVER_MESSAGE_GETGUTTER_H
