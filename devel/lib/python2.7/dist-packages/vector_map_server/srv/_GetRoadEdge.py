# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vector_map_server/GetRoadEdgeRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import autoware_msgs.msg
import geometry_msgs.msg
import std_msgs.msg

class GetRoadEdgeRequest(genpy.Message):
  _md5sum = "ae97823c56512a205c88cf57b8d90385"
  _type = "vector_map_server/GetRoadEdgeRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/PoseStamped pose
autoware_msgs/Lane waypoints

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: autoware_msgs/Lane
Header header
int32 increment
int32 lane_id
Waypoint[] waypoints

uint32 lane_index
float32 cost
float32 closest_object_distance
float32 closest_object_velocity
bool is_blocked

================================================================================
MSG: autoware_msgs/Waypoint
# global id
int32 gid 
# local id
int32 lid
geometry_msgs/PoseStamped pose
geometry_msgs/TwistStamped twist
DTLane dtlane
int32 change_flag
WaypointState wpstate

uint32 lane_id
uint32 left_lane_id
uint32 right_lane_id
uint32 stop_line_id
float32 cost
float32 time_cost

# Lane Direction
# FORWARD				= 0
# FORWARD_LEFT	 		= 1
# FORWARD_RIGHT			= 2
# BACKWARD				= 3 
# BACKWARD_LEFT			= 4
# BACKWARD_RIGHT		= 5
# STANDSTILL	 		= 6
uint32 direction
================================================================================
MSG: geometry_msgs/TwistStamped
# A twist with reference coordinate frame and timestamp
Header header
Twist twist

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: autoware_msgs/DTLane
float64 dist
float64 dir
float64 apara
float64 r
float64 slope
float64 cant
float64 lw
float64 rw

================================================================================
MSG: autoware_msgs/WaypointState
int32 aid
uint8 NULLSTATE=0
uint8 lanechange_state

uint8 steering_state
uint8 STR_LEFT=1
uint8 STR_RIGHT=2
uint8 STR_STRAIGHT=3

uint8 accel_state
uint8 stopline_state
  uint8 TYPE_NULL=0
  uint8 TYPE_STOPLINE=1
  uint8 TYPE_STOP=2
# 1 is stopline, 2 is stop which 2 can only be released manually.
uint64 event_state
"""
  __slots__ = ['pose','waypoints']
  _slot_types = ['geometry_msgs/PoseStamped','autoware_msgs/Lane']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pose,waypoints

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetRoadEdgeRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.waypoints is None:
        self.waypoints = autoware_msgs.msg.Lane()
    else:
      self.pose = geometry_msgs.msg.PoseStamped()
      self.waypoints = autoware_msgs.msg.Lane()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.waypoints.header.seq, _x.waypoints.header.stamp.secs, _x.waypoints.header.stamp.nsecs))
      _x = self.waypoints.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.waypoints.increment, _x.waypoints.lane_id))
      length = len(self.waypoints.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints.waypoints:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.gid, _x.lid))
        _v1 = val1.pose
        _v2 = _v1.header
        buff.write(_get_struct_I().pack(_v2.seq))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v4 = _v1.pose
        _v5 = _v4.position
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v6 = _v4.orientation
        _x = _v6
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v7 = val1.twist
        _v8 = _v7.header
        buff.write(_get_struct_I().pack(_v8.seq))
        _v9 = _v8.stamp
        _x = _v9
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v8.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v10 = _v7.twist
        _v11 = _v10.linear
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = _v10.angular
        _x = _v12
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v13 = val1.dtlane
        _x = _v13
        buff.write(_get_struct_8d().pack(_x.dist, _x.dir, _x.apara, _x.r, _x.slope, _x.cant, _x.lw, _x.rw))
        buff.write(_get_struct_i().pack(val1.change_flag))
        _v14 = val1.wpstate
        _x = _v14
        buff.write(_get_struct_i4BQ().pack(_x.aid, _x.lanechange_state, _x.steering_state, _x.accel_state, _x.stopline_state, _x.event_state))
        _x = val1
        buff.write(_get_struct_4I2fI().pack(_x.lane_id, _x.left_lane_id, _x.right_lane_id, _x.stop_line_id, _x.cost, _x.time_cost, _x.direction))
      _x = self
      buff.write(_get_struct_I3fB().pack(_x.waypoints.lane_index, _x.waypoints.cost, _x.waypoints.closest_object_distance, _x.waypoints.closest_object_velocity, _x.waypoints.is_blocked))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.waypoints is None:
        self.waypoints = autoware_msgs.msg.Lane()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.waypoints.header.seq, _x.waypoints.header.stamp.secs, _x.waypoints.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.waypoints.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.waypoints.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.waypoints.increment, _x.waypoints.lane_id,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints.waypoints = []
      for i in range(0, length):
        val1 = autoware_msgs.msg.Waypoint()
        _x = val1
        start = end
        end += 8
        (_x.gid, _x.lid,) = _get_struct_2i().unpack(str[start:end])
        _v15 = val1.pose
        _v16 = _v15.header
        start = end
        end += 4
        (_v16.seq,) = _get_struct_I().unpack(str[start:end])
        _v17 = _v16.stamp
        _x = _v17
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v16.frame_id = str[start:end].decode('utf-8')
        else:
          _v16.frame_id = str[start:end]
        _v18 = _v15.pose
        _v19 = _v18.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v20 = _v18.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v21 = val1.twist
        _v22 = _v21.header
        start = end
        end += 4
        (_v22.seq,) = _get_struct_I().unpack(str[start:end])
        _v23 = _v22.stamp
        _x = _v23
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v22.frame_id = str[start:end].decode('utf-8')
        else:
          _v22.frame_id = str[start:end]
        _v24 = _v21.twist
        _v25 = _v24.linear
        _x = _v25
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v26 = _v24.angular
        _x = _v26
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v27 = val1.dtlane
        _x = _v27
        start = end
        end += 64
        (_x.dist, _x.dir, _x.apara, _x.r, _x.slope, _x.cant, _x.lw, _x.rw,) = _get_struct_8d().unpack(str[start:end])
        start = end
        end += 4
        (val1.change_flag,) = _get_struct_i().unpack(str[start:end])
        _v28 = val1.wpstate
        _x = _v28
        start = end
        end += 16
        (_x.aid, _x.lanechange_state, _x.steering_state, _x.accel_state, _x.stopline_state, _x.event_state,) = _get_struct_i4BQ().unpack(str[start:end])
        _x = val1
        start = end
        end += 28
        (_x.lane_id, _x.left_lane_id, _x.right_lane_id, _x.stop_line_id, _x.cost, _x.time_cost, _x.direction,) = _get_struct_4I2fI().unpack(str[start:end])
        self.waypoints.waypoints.append(val1)
      _x = self
      start = end
      end += 17
      (_x.waypoints.lane_index, _x.waypoints.cost, _x.waypoints.closest_object_distance, _x.waypoints.closest_object_velocity, _x.waypoints.is_blocked,) = _get_struct_I3fB().unpack(str[start:end])
      self.waypoints.is_blocked = bool(self.waypoints.is_blocked)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs))
      _x = self.pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.waypoints.header.seq, _x.waypoints.header.stamp.secs, _x.waypoints.header.stamp.nsecs))
      _x = self.waypoints.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2i().pack(_x.waypoints.increment, _x.waypoints.lane_id))
      length = len(self.waypoints.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints.waypoints:
        _x = val1
        buff.write(_get_struct_2i().pack(_x.gid, _x.lid))
        _v29 = val1.pose
        _v30 = _v29.header
        buff.write(_get_struct_I().pack(_v30.seq))
        _v31 = _v30.stamp
        _x = _v31
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v30.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v32 = _v29.pose
        _v33 = _v32.position
        _x = _v33
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v34 = _v32.orientation
        _x = _v34
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v35 = val1.twist
        _v36 = _v35.header
        buff.write(_get_struct_I().pack(_v36.seq))
        _v37 = _v36.stamp
        _x = _v37
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v36.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v38 = _v35.twist
        _v39 = _v38.linear
        _x = _v39
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v40 = _v38.angular
        _x = _v40
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v41 = val1.dtlane
        _x = _v41
        buff.write(_get_struct_8d().pack(_x.dist, _x.dir, _x.apara, _x.r, _x.slope, _x.cant, _x.lw, _x.rw))
        buff.write(_get_struct_i().pack(val1.change_flag))
        _v42 = val1.wpstate
        _x = _v42
        buff.write(_get_struct_i4BQ().pack(_x.aid, _x.lanechange_state, _x.steering_state, _x.accel_state, _x.stopline_state, _x.event_state))
        _x = val1
        buff.write(_get_struct_4I2fI().pack(_x.lane_id, _x.left_lane_id, _x.right_lane_id, _x.stop_line_id, _x.cost, _x.time_cost, _x.direction))
      _x = self
      buff.write(_get_struct_I3fB().pack(_x.waypoints.lane_index, _x.waypoints.cost, _x.waypoints.closest_object_distance, _x.waypoints.closest_object_velocity, _x.waypoints.is_blocked))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pose is None:
        self.pose = geometry_msgs.msg.PoseStamped()
      if self.waypoints is None:
        self.waypoints = autoware_msgs.msg.Lane()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.pose.header.seq, _x.pose.header.stamp.secs, _x.pose.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pose.pose.position.x, _x.pose.pose.position.y, _x.pose.pose.position.z, _x.pose.pose.orientation.x, _x.pose.pose.orientation.y, _x.pose.pose.orientation.z, _x.pose.pose.orientation.w, _x.waypoints.header.seq, _x.waypoints.header.stamp.secs, _x.waypoints.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.waypoints.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.waypoints.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.waypoints.increment, _x.waypoints.lane_id,) = _get_struct_2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints.waypoints = []
      for i in range(0, length):
        val1 = autoware_msgs.msg.Waypoint()
        _x = val1
        start = end
        end += 8
        (_x.gid, _x.lid,) = _get_struct_2i().unpack(str[start:end])
        _v43 = val1.pose
        _v44 = _v43.header
        start = end
        end += 4
        (_v44.seq,) = _get_struct_I().unpack(str[start:end])
        _v45 = _v44.stamp
        _x = _v45
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v44.frame_id = str[start:end].decode('utf-8')
        else:
          _v44.frame_id = str[start:end]
        _v46 = _v43.pose
        _v47 = _v46.position
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v48 = _v46.orientation
        _x = _v48
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v49 = val1.twist
        _v50 = _v49.header
        start = end
        end += 4
        (_v50.seq,) = _get_struct_I().unpack(str[start:end])
        _v51 = _v50.stamp
        _x = _v51
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v50.frame_id = str[start:end].decode('utf-8')
        else:
          _v50.frame_id = str[start:end]
        _v52 = _v49.twist
        _v53 = _v52.linear
        _x = _v53
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v54 = _v52.angular
        _x = _v54
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v55 = val1.dtlane
        _x = _v55
        start = end
        end += 64
        (_x.dist, _x.dir, _x.apara, _x.r, _x.slope, _x.cant, _x.lw, _x.rw,) = _get_struct_8d().unpack(str[start:end])
        start = end
        end += 4
        (val1.change_flag,) = _get_struct_i().unpack(str[start:end])
        _v56 = val1.wpstate
        _x = _v56
        start = end
        end += 16
        (_x.aid, _x.lanechange_state, _x.steering_state, _x.accel_state, _x.stopline_state, _x.event_state,) = _get_struct_i4BQ().unpack(str[start:end])
        _x = val1
        start = end
        end += 28
        (_x.lane_id, _x.left_lane_id, _x.right_lane_id, _x.stop_line_id, _x.cost, _x.time_cost, _x.direction,) = _get_struct_4I2fI().unpack(str[start:end])
        self.waypoints.waypoints.append(val1)
      _x = self
      start = end
      end += 17
      (_x.waypoints.lane_index, _x.waypoints.cost, _x.waypoints.closest_object_distance, _x.waypoints.closest_object_velocity, _x.waypoints.is_blocked,) = _get_struct_I3fB().unpack(str[start:end])
      self.waypoints.is_blocked = bool(self.waypoints.is_blocked)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8d = None
def _get_struct_8d():
    global _struct_8d
    if _struct_8d is None:
        _struct_8d = struct.Struct("<8d")
    return _struct_8d
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_i4BQ = None
def _get_struct_i4BQ():
    global _struct_i4BQ
    if _struct_i4BQ is None:
        _struct_i4BQ = struct.Struct("<i4BQ")
    return _struct_i4BQ
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_4I2fI = None
def _get_struct_4I2fI():
    global _struct_4I2fI
    if _struct_4I2fI is None:
        _struct_4I2fI = struct.Struct("<4I2fI")
    return _struct_4I2fI
_struct_I3fB = None
def _get_struct_I3fB():
    global _struct_I3fB
    if _struct_I3fB is None:
        _struct_I3fB = struct.Struct("<I3fB")
    return _struct_I3fB
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vector_map_server/GetRoadEdgeResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import vector_map_msgs.msg

class GetRoadEdgeResponse(genpy.Message):
  _md5sum = "bd9a2abeb71ea61e315c29d2d466b6cb"
  _type = "vector_map_server/GetRoadEdgeResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """vector_map_msgs/RoadEdgeArray objects


================================================================================
MSG: vector_map_msgs/RoadEdgeArray
Header header
RoadEdge[] data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: vector_map_msgs/RoadEdge
# Ver 1.00
int32 id
int32 lid
int32 linkid
"""
  __slots__ = ['objects']
  _slot_types = ['vector_map_msgs/RoadEdgeArray']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       objects

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetRoadEdgeResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.objects is None:
        self.objects = vector_map_msgs.msg.RoadEdgeArray()
    else:
      self.objects = vector_map_msgs.msg.RoadEdgeArray()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.objects.header.seq, _x.objects.header.stamp.secs, _x.objects.header.stamp.nsecs))
      _x = self.objects.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.objects.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects.data:
        _x = val1
        buff.write(_get_struct_3i().pack(_x.id, _x.lid, _x.linkid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.objects is None:
        self.objects = vector_map_msgs.msg.RoadEdgeArray()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.objects.header.seq, _x.objects.header.stamp.secs, _x.objects.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objects.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.objects.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.objects.data = []
      for i in range(0, length):
        val1 = vector_map_msgs.msg.RoadEdge()
        _x = val1
        start = end
        end += 12
        (_x.id, _x.lid, _x.linkid,) = _get_struct_3i().unpack(str[start:end])
        self.objects.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.objects.header.seq, _x.objects.header.stamp.secs, _x.objects.header.stamp.nsecs))
      _x = self.objects.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.objects.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.objects.data:
        _x = val1
        buff.write(_get_struct_3i().pack(_x.id, _x.lid, _x.linkid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.objects is None:
        self.objects = vector_map_msgs.msg.RoadEdgeArray()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.objects.header.seq, _x.objects.header.stamp.secs, _x.objects.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objects.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.objects.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.objects.data = []
      for i in range(0, length):
        val1 = vector_map_msgs.msg.RoadEdge()
        _x = val1
        start = end
        end += 12
        (_x.id, _x.lid, _x.linkid,) = _get_struct_3i().unpack(str[start:end])
        self.objects.data.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i
class GetRoadEdge(object):
  _type          = 'vector_map_server/GetRoadEdge'
  _md5sum = '34fec351d04e3e6f93731a4a41785144'
  _request_class  = GetRoadEdgeRequest
  _response_class = GetRoadEdgeResponse
