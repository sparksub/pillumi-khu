import 'package:flutter/cupertino.dart';

import '../../api/class/pill.dart';
import '../card/build_another_pill_card.dart';

Column BuildOtherPill(List<Pill> otherPill, BuildContext context) {
  return Column(
    children: [
      Container(
        alignment: Alignment.bottomLeft,
        padding: const EdgeInsets.only(
            left: 10.0, right: 10.0, top: 20.0, bottom: 5.0),
        child: const Text("찾고 있는 약이 아닌가요? \n비슷한 약도 확인해보세요.",
          style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20),
        ),
      ),
      Column(
          children: otherPill.map<Widget>(
                  (data)=>BuildAnotherPillCard(context, data)
          ).toList()
      ),
    ],
  );
}