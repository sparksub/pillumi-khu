import 'package:flutter/material.dart';

Card BuildAnotherPillCard(title, name, img) {
  return Card(
      elevation: 2.0,
      child: Container(
        alignment: Alignment.centerLeft,
        padding: const EdgeInsets.all(10.0),
        child: ListTile(
          leading: Image(
            image: AssetImage(img),
            height: 60,
          ),
          title: Text(title,
            style: const TextStyle(
                fontWeight: FontWeight.bold,
                fontSize: 20),
          ),
          subtitle: Text(name,
            style: const TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 17
            ),
          ),
        ),
      )
  );
}