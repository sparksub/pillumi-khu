import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

class ResultScreenWidget extends StatelessWidget {
  const ResultScreenWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('결과화면'),
      ),
      body: Container(
          width: double.infinity,
          height: double.infinity,
          color: palette.blue,
          child: const Text("good!")
      ),
    );
  }
}