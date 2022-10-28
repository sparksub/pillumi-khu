import 'package:flutter/material.dart';

Card buildPillInfoCard(title, text) {
  return Card(
      elevation: 2.0,
      child: Container(
        alignment: Alignment.topLeft,
        padding: const EdgeInsets.all(10.0),
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title,
                style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 17),
              ),
              const SizedBox(height: 8.0),
              Padding(
                padding: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Text(text,
                  softWrap: true,
                  style: const TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 15),
                ),
              ),
            ],
          ),
        ),
      )
  );
}

Card buildPillInfoPhotoCard(title, imgUrl) {
  return Card(
      elevation: 2.0,
      child: Container(
        alignment: Alignment.topLeft,
        padding: const EdgeInsets.all(10.0),
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title,
                style: const TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 17),
              ),
              const SizedBox(height: 8.0),
              Padding(
                padding: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Image(
                  image: AssetImage(imgUrl),
                  height: 60,
                ),
              ),
            ],
          ),
        ),
      )
  );
}