import 'package:flutter/material.dart';

Card BuildAnotherPillCard(title, name) {
  return Card(
      elevation: 2.0,
      child: Container(
        alignment: Alignment.centerLeft,
        padding: const EdgeInsets.all(10.0),
        child: ListTile(
          leading: Image(
            image: AssetImage('assets/pill-icon-nobackground.png'),
            height: 60,
          ),
          title: Text(title,
            style: const TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 17),
          ),
          subtitle: Text(name,
            style: const TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 15
            ),
          ),
        ),
      )
  );
}