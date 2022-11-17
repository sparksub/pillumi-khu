import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

import 'class/pill_list.dart';

String base_url = 'http://172.16.23.42:5001';

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