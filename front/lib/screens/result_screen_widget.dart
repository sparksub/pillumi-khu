import 'package:flutter/material.dart';

class ResultScreenWidget extends StatelessWidget {
  const ResultScreenWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Second Screen'),
      ),
      body: Container(
          width: double.infinity,
          height: double.infinity,
          color: Colors.amber,
          child: const Text("good!")
      ),
    );
  }
}