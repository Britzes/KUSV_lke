
(cl:in-package :asdf)

(defsystem "rs232_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "rs232Data" :depends-on ("_package_rs232Data"))
    (:file "_package_rs232Data" :depends-on ("_package"))
    (:file "rs232Info" :depends-on ("_package_rs232Info"))
    (:file "_package_rs232Info" :depends-on ("_package"))
    (:file "rs232Packet" :depends-on ("_package_rs232Packet"))
    (:file "_package_rs232Packet" :depends-on ("_package"))
  ))