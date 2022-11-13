import 'package:permission_handler/permission_handler.dart';

Future<void> requestCameraPermission() async {
  final serviceStatus = await Permission.camera.isGranted ;
  bool isCameraOn = serviceStatus == ServiceStatus.enabled;

  final status = await Permission.camera.request();

  if (status == PermissionStatus.granted) {
    print('Permission Granted');
  } else if (status == PermissionStatus.denied) {
    print('Permission denied');
  } else if (status == PermissionStatus.permanentlyDenied) {
    print('Permission Permanently Denied');
    await openAppSettings();
  }
}

Future<void> requestPhotosPermission() async {
  final serviceStatusPhotos = await Permission.photos.isGranted ;
  bool isPhoto = serviceStatusPhotos == ServiceStatus.enabled;

  final status = await Permission.photos.request();

  if (status == PermissionStatus.granted) {
    print('Permission Granted');
  } else if (status == PermissionStatus.denied) {
    print('Permission denied');
  } else if (status == PermissionStatus.permanentlyDenied) {
    print('Permission Permanently Denied');
    await openAppSettings();
  }
}