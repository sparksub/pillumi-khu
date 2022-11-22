import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

Center buildProgress() {
  return Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const Text('검색 중입니다.',
          style: TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 25,
            color: Colors.black,
          ),
        ),
        SizedBox(height: 20.0),
        CircularProgressIndicator(
          valueColor: AlwaysStoppedAnimation<Color>(palette.blue),
        ),
      ],
    ),
  );
}