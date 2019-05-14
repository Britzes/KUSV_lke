
"use strict";

let ColorSet = require('./ColorSet.js');
let TrafficLight = require('./TrafficLight.js');
let AccelCmd = require('./AccelCmd.js');
let IndicatorCmd = require('./IndicatorCmd.js');
let Lane = require('./Lane.js');
let ImageRect = require('./ImageRect.js');
let VscanTrackedArray = require('./VscanTrackedArray.js');
let ScanImage = require('./ScanImage.js');
let Waypoint = require('./Waypoint.js');
let VehicleStatus = require('./VehicleStatus.js');
let ExtractedPosition = require('./ExtractedPosition.js');
let SyncTimeMonitor = require('./SyncTimeMonitor.js');
let CloudClusterArray = require('./CloudClusterArray.js');
let WaypointState = require('./WaypointState.js');
let NDTStat = require('./NDTStat.js');
let ObjLabel = require('./ObjLabel.js');
let DTLane = require('./DTLane.js');
let ValueSet = require('./ValueSet.js');
let ImageLaneObjects = require('./ImageLaneObjects.js');
let ProjectionMatrix = require('./ProjectionMatrix.js');
let CloudCluster = require('./CloudCluster.js');
let ControlCommand = require('./ControlCommand.js');
let VehicleCmd = require('./VehicleCmd.js');
let LaneArray = require('./LaneArray.js');
let ImageObjTracked = require('./ImageObjTracked.js');
let ImageObj = require('./ImageObj.js');
let GeometricRectangle = require('./GeometricRectangle.js');
let SyncTimeDiff = require('./SyncTimeDiff.js');
let ObjPose = require('./ObjPose.js');
let BrakeCmd = require('./BrakeCmd.js');
let PointsImage = require('./PointsImage.js');
let SteerCmd = require('./SteerCmd.js');
let LampCmd = require('./LampCmd.js');
let TrafficLightResultArray = require('./TrafficLightResultArray.js');
let DetectedObjectArray = require('./DetectedObjectArray.js');
let State = require('./State.js');
let DetectedObject = require('./DetectedObject.js');
let ICPStat = require('./ICPStat.js');
let ImageObjRanged = require('./ImageObjRanged.js');
let ControlCommandStamped = require('./ControlCommandStamped.js');
let StateCmd = require('./StateCmd.js');
let AdjustXY = require('./AdjustXY.js');
let VscanTracked = require('./VscanTracked.js');
let Signals = require('./Signals.js');
let ImageObjects = require('./ImageObjects.js');
let ImageRectRanged = require('./ImageRectRanged.js');
let TunedResult = require('./TunedResult.js');
let CameraExtrinsic = require('./CameraExtrinsic.js');
let RemoteCmd = require('./RemoteCmd.js');
let Centroids = require('./Centroids.js');
let TrafficLightResult = require('./TrafficLightResult.js');

module.exports = {
  ColorSet: ColorSet,
  TrafficLight: TrafficLight,
  AccelCmd: AccelCmd,
  IndicatorCmd: IndicatorCmd,
  Lane: Lane,
  ImageRect: ImageRect,
  VscanTrackedArray: VscanTrackedArray,
  ScanImage: ScanImage,
  Waypoint: Waypoint,
  VehicleStatus: VehicleStatus,
  ExtractedPosition: ExtractedPosition,
  SyncTimeMonitor: SyncTimeMonitor,
  CloudClusterArray: CloudClusterArray,
  WaypointState: WaypointState,
  NDTStat: NDTStat,
  ObjLabel: ObjLabel,
  DTLane: DTLane,
  ValueSet: ValueSet,
  ImageLaneObjects: ImageLaneObjects,
  ProjectionMatrix: ProjectionMatrix,
  CloudCluster: CloudCluster,
  ControlCommand: ControlCommand,
  VehicleCmd: VehicleCmd,
  LaneArray: LaneArray,
  ImageObjTracked: ImageObjTracked,
  ImageObj: ImageObj,
  GeometricRectangle: GeometricRectangle,
  SyncTimeDiff: SyncTimeDiff,
  ObjPose: ObjPose,
  BrakeCmd: BrakeCmd,
  PointsImage: PointsImage,
  SteerCmd: SteerCmd,
  LampCmd: LampCmd,
  TrafficLightResultArray: TrafficLightResultArray,
  DetectedObjectArray: DetectedObjectArray,
  State: State,
  DetectedObject: DetectedObject,
  ICPStat: ICPStat,
  ImageObjRanged: ImageObjRanged,
  ControlCommandStamped: ControlCommandStamped,
  StateCmd: StateCmd,
  AdjustXY: AdjustXY,
  VscanTracked: VscanTracked,
  Signals: Signals,
  ImageObjects: ImageObjects,
  ImageRectRanged: ImageRectRanged,
  TunedResult: TunedResult,
  CameraExtrinsic: CameraExtrinsic,
  RemoteCmd: RemoteCmd,
  Centroids: Centroids,
  TrafficLightResult: TrafficLightResult,
};
