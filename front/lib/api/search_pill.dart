import 'dart:io';

import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

String base_url = 'http://172.30.1.46:5001';

class PillList{
  final Pill main;
  final List<Pill> others;

  PillList({required this.main, required this.others});

  factory PillList.fromJson(Map<String, dynamic> pillMap){
    var list = pillMap['OtherPill'] as List;
    List<Pill> othersPill = list.map((i)=> Pill.fromJson(i)).toList();

    return PillList(
        main: Pill.fromJson(pillMap['ResultPill']),
        others: othersPill,
    );
  }

}

class Pill {
  final String itemName;
  final String emtpName;
  final String className;
  final String efficacy;
  final String dosage;
  final String atpnWarnQesitm;
  final String atpnQesitm;
  final String seQesitm;
  final String depoditMetodQesirm;
  final String pillImg;
  final String intrcQesitm;

  // final List<String> infoImg;

  Pill({
    required this.itemName,
    required this.emtpName,
    required this.className,
    required this.efficacy,
    required this.dosage,
    required this.atpnWarnQesitm,
    required this.atpnQesitm,
    required this.seQesitm,
    required this.depoditMetodQesirm,
    required this.pillImg,
    required this.intrcQesitm
    // required this.infoImg
  });

  factory Pill.fromJson(Map<String, dynamic> pillMap){
    // var infoImgFromJson = pillMap['InfoImg'];
    // List<String> infoImg = new List<String>.from(infoImgFromJson);

    return Pill(
      itemName: pillMap['ITEM_NAME'],
      emtpName: pillMap['ENTP_NAME'],
      className: pillMap['CLASS_NAME'],
      efficacy: pillMap['Efficacy'],
      dosage: pillMap['Dosage'],
      atpnWarnQesitm: pillMap['AtpnWarnQesitm'],
      atpnQesitm: pillMap['AtpnQesitm'],
      intrcQesitm: pillMap["IntrcQesitm"],
      seQesitm: pillMap['SeQesitm'],
      depoditMetodQesirm: pillMap['DepositMethodQesitm'],
      pillImg: pillMap['PillImg'],
      // infoImg: infoImg,
    );
  }
}

Future<PillList> SearchPill(base64frontImg, base64backImg) async {
  Map<String, String> headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  Uri uri = Uri.parse('$base_url/pillsearch/');
  // print("good");
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
    final pillMap = await json.decode(response.body);
    return PillList.fromJson(pillMap);
  }
  throw Exception('검색 실패');
}