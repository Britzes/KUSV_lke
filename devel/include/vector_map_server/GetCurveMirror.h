// Generated by gencpp from file vector_map_server/GetCurveMirror.msg
// DO NOT EDIT!


#ifndef VECTOR_MAP_SERVER_MESSAGE_GETCURVEMIRROR_H
#define VECTOR_MAP_SERVER_MESSAGE_GETCURVEMIRROR_H

#include <ros/service_traits.h>


#include <vector_map_server/GetCurveMirrorRequest.h>
#include <vector_map_server/GetCurveMirrorResponse.h>


namespace vector_map_server
{

struct GetCurveMirror
{

typedef GetCurveMirrorRequest Request;
typedef GetCurveMirrorResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetCurveMirror
} // namespace vector_map_server


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::vector_map_server::GetCurveMirror > {
  static const char* value()
  {
    return "09102c9b889240ac7da1878d7a90e711";
  }

  static const char* value(const ::vector_map_server::GetCurveMirror&) { return value(); }
};

template<>
struct DataType< ::vector_map_server::GetCurveMirror > {
  static const char* value()
  {
    return "vector_map_server/GetCurveMirror";
  }

  static const char* value(const ::vector_map_server::GetCurveMirror&) { return value(); }
};


// service_traits::MD5Sum< ::vector_map_server::GetCurveMirrorRequest> should match 
// service_traits::MD5Sum< ::vector_map_server::GetCurveMirror > 
template<>
struct MD5Sum< ::vector_map_server::GetCurveMirrorRequest>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetCurveMirror >::value();
  }
  static const char* value(const ::vector_map_server::GetCurveMirrorRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetCurveMirrorRequest> should match 
// service_traits::DataType< ::vector_map_server::GetCurveMirror > 
template<>
struct DataType< ::vector_map_server::GetCurveMirrorRequest>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetCurveMirror >::value();
  }
  static const char* value(const ::vector_map_server::GetCurveMirrorRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::vector_map_server::GetCurveMirrorResponse> should match 
// service_traits::MD5Sum< ::vector_map_server::GetCurveMirror > 
template<>
struct MD5Sum< ::vector_map_server::GetCurveMirrorResponse>
{
  static const char* value()
  {
    return MD5Sum< ::vector_map_server::GetCurveMirror >::value();
  }
  static const char* value(const ::vector_map_server::GetCurveMirrorResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::vector_map_server::GetCurveMirrorResponse> should match 
// service_traits::DataType< ::vector_map_server::GetCurveMirror > 
template<>
struct DataType< ::vector_map_server::GetCurveMirrorResponse>
{
  static const char* value()
  {
    return DataType< ::vector_map_server::GetCurveMirror >::value();
  }
  static const char* value(const ::vector_map_server::GetCurveMirrorResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // VECTOR_MAP_SERVER_MESSAGE_GETCURVEMIRROR_H
