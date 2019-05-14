; Auto-generated. Do not edit!


(cl:in-package rs232_msgs-msg)


;//! \htmlinclude rs232Data.msg.html

(cl:defclass <rs232Data> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (count
    :reader count
    :initarg :count
    :type cl:integer
    :initform 0)
   (id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (time
    :reader time
    :initarg :time
    :type cl:integer
    :initform 0)
   (flag
    :reader flag
    :initarg :flag
    :type cl:fixnum
    :initform 0))
)

(cl:defclass rs232Data (<rs232Data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <rs232Data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'rs232Data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rs232_msgs-msg:<rs232Data> is deprecated: use rs232_msgs-msg:rs232Data instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <rs232Data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rs232_msgs-msg:header-val is deprecated.  Use rs232_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'count-val :lambda-list '(m))
(cl:defmethod count-val ((m <rs232Data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rs232_msgs-msg:count-val is deprecated.  Use rs232_msgs-msg:count instead.")
  (count m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <rs232Data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rs232_msgs-msg:id-val is deprecated.  Use rs232_msgs-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'time-val :lambda-list '(m))
(cl:defmethod time-val ((m <rs232Data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rs232_msgs-msg:time-val is deprecated.  Use rs232_msgs-msg:time instead.")
  (time m))

(cl:ensure-generic-function 'flag-val :lambda-list '(m))
(cl:defmethod flag-val ((m <rs232Data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rs232_msgs-msg:flag-val is deprecated.  Use rs232_msgs-msg:flag instead.")
  (flag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <rs232Data>) ostream)
  "Serializes a message object of type '<rs232Data>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'count)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'time)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'flag)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'flag)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <rs232Data>) istream)
  "Deserializes a message object of type '<rs232Data>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'count)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'time)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'flag)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'flag)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<rs232Data>)))
  "Returns string type for a message object of type '<rs232Data>"
  "rs232_msgs/rs232Data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'rs232Data)))
  "Returns string type for a message object of type 'rs232Data"
  "rs232_msgs/rs232Data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<rs232Data>)))
  "Returns md5sum for a message object of type '<rs232Data>"
  "3364528f120c0215964c8aca9e410a19")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'rs232Data)))
  "Returns md5sum for a message object of type 'rs232Data"
  "3364528f120c0215964c8aca9e410a19")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<rs232Data>)))
  "Returns full string definition for message of type '<rs232Data>"
  (cl:format cl:nil "Header header~%uint32 count~%uint32 id~%uint32 time~%uint16 flag~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'rs232Data)))
  "Returns full string definition for message of type 'rs232Data"
  (cl:format cl:nil "Header header~%uint32 count~%uint32 id~%uint32 time~%uint16 flag~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <rs232Data>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <rs232Data>))
  "Converts a ROS message object to a list"
  (cl:list 'rs232Data
    (cl:cons ':header (header msg))
    (cl:cons ':count (count msg))
    (cl:cons ':id (id msg))
    (cl:cons ':time (time msg))
    (cl:cons ':flag (flag msg))
))
