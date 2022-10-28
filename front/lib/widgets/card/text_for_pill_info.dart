import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

Padding textForPillInfo(text1, text2) {
  return Padding(
    padding: const EdgeInsets.only(
        left: 20.0,
        right: 20.0,
        top: 5.0,
        bottom: 5.0
    ),
    child: Row(
      children: [
        Expanded(
          flex: 3,
          child: Text(text1,
            textAlign: TextAlign.start,
            style: TextStyle(
                fontWeight: FontWeight.w500,
                color: palette.darkBlue,
                fontSize: 15
            ),
          ),
        ),
        Expanded(
          flex: 7,
          child: Text(text2,
            textAlign: TextAlign.start,
            style: TextStyle(
                fontWeight: FontWeight.w600,
                color: palette.black,
                fontSize: 15
            ),
          ),
        ),
      ],
    ),
  );
}