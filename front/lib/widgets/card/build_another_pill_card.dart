import 'package:flutter/material.dart';

import '../../api/search_pill.dart';
import '../../screens/similar_screen_widget.dart';

Card BuildAnotherPillCard(BuildContext context, Pill pill) {
  return Card(
      elevation: 2.0,
      child: InkWell(
        onTap: ()=>{
          goToSimilarPage(context, pill)
        },
        child: Container(
          alignment: Alignment.centerLeft,
          padding: const EdgeInsets.all(5.0),
          child: ListTile(
            leading: Container(
              height: 60,
              child: Image.network(pill.pillImg.toString(),
                  fit: BoxFit.fill
              ),
            ),
            title: Text(pill.className.toString(),
              style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 20),
            ),
            subtitle: Text(pill.itemName.toString(),
              style: const TextStyle(
                  fontWeight: FontWeight.w500,
                  fontSize: 17
              ),
            ),
          ),
        ),
      )
  );
}

void goToSimilarPage(BuildContext context, Pill pill) {
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => SimilarScreenWidget(pill)),
  );
}