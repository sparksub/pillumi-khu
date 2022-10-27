import 'package:flutter/material.dart';
import 'package:front/screens/main_screen_widget.dart';
import 'package:front/util/palette.dart' as palette;

void main() {
  runApp(const PillumiApp());
}

class PillumiApp extends StatelessWidget {
  const PillumiApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Pillumi App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: palette.white,
      ),
      home: MainScreenWidget(),
    );
  }
}