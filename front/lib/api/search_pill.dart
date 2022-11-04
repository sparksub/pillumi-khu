import 'dart:io';

import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

String base_url = 'http://172.16.23.198:5001';

class Pill {
  final String itemName;
  final String emtpName;
  final String className;
  final String efficacy;
  final String dosage;

  final List<String> infoImg;

  Pill({
    required this.itemName,
    required this.emtpName,
    required this.className,
    required this.efficacy,
    required this.dosage,
    required this.infoImg});

  factory Pill.fromJson(Map<String, dynamic> pillMap){
    var infoImgFromJson = pillMap['InfoImg'];
    List<String> infoImg = new List<String>.from(infoImgFromJson);

    return Pill(
      itemName: pillMap['ITEM_NAME'],
      emtpName: pillMap['ENTP_NAME'],
      className: pillMap['CLASS_NAME'],
      efficacy: pillMap['Efficacy'],
      dosage: pillMap['Dosage'],
      infoImg: infoImg,
    );
  }
}

Future<Pill> SearchPill(pillImageFront, pillImageBack) async {
  Map<String, String> headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  File frontImgFile = File(pillImageFront!.path);
  File backImgFile = File(pillImageBack!.path);
  List<int> frontImgBytes = frontImgFile.readAsBytesSync();
  List<int> backImgBytes = backImgFile.readAsBytesSync();

  String base64frontImg = base64Encode(frontImgBytes);
  String base64backImg = base64Encode(backImgBytes);

  Uri uri = Uri.parse('$base_url/pillsearch/');
  print(uri);
  http.Response response = await http.post(
    uri,
    headers: headers,
    body: jsonEncode([
        {
          'image_front': base64frontImg,
          'image_back': base64backImg
        }
      ])
  );

  if(response.statusCode == 200){
    final pillMap = json.decode(response.body);
    print(pillMap);
    return Pill.fromJson(pillMap);
  }
  throw Exception('검색 실패');
}