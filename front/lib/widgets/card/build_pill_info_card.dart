import 'package:flutter/material.dart';


// We didn't use this card widget.
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
                    fontSize: 20),
              ),
              const SizedBox(height: 8.0),
              Padding(
                padding: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Text(text,
                  softWrap: true,
                  style: const TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 17),
                ),
              ),
            ],
          ),
        ),
      )
  );
}

Card buildPillInfoPhotoCard(String title, List<dynamic> imgUrlList) {
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
                    fontSize: 20),
              ),
              const SizedBox(height: 8.0),
              Row(
                children: imgUrlList.map<Widget>((img)=> Padding(
                      padding: const EdgeInsets.only(left: 8.0),
                      child: Image(
                        image: AssetImage("assets/pictogram/$img.jpg"),
                        height: 100)
                )).toList()
              ),
            ],
          ),
        ),
      )
  );
}


Card buildPillInfoPhotoCardWithText(String title, String text, List<dynamic> imgUrlList) {
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
                    fontSize: 20),
              ),
              const SizedBox(height: 8.0),
              Row(
                  children: imgUrlList.map<Widget>((img)=> Padding(
                      padding: const EdgeInsets.only(left: 8.0),
                      child: Image(
                          image: AssetImage("assets/pictogram/$img.jpg"),
                          height: 100)
                  )).toList()
              ),
              const SizedBox(height: 8.0),
              Padding(
                padding: const EdgeInsets.only(left: 8.0, right: 8.0),
                child: Text(text,
                  softWrap: true,
                  style: const TextStyle(
                      fontWeight: FontWeight.w400,
                      fontSize: 17),
                ),
              ),
            ],
          ),
        ),
      )
  );
}