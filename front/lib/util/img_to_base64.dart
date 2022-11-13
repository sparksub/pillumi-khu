import 'dart:io';
import 'dart:convert';

List<String> imgToBase64 (pillImageFront, pillImageBack) {
  File frontImgFile = File(pillImageFront!.path);
  File backImgFile = File(pillImageBack!.path);

  List<int> frontImgBytes = frontImgFile.readAsBytesSync();
  List<int> backImgBytes = backImgFile.readAsBytesSync();

  String base64frontImg = base64Encode(frontImgBytes);
  String base64backImg = base64Encode(backImgBytes);
  return [base64frontImg, base64backImg];
}