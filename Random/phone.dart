// main.dart - Flutter
import 'package:flutter/material.dart';

void main() => runApp(GymChecklistApp());

class GymChecklistApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Gym Checklist',
      home: GymChecklistPage(),
    );
  }
}

class GymChecklistPage extends StatefulWidget {
  @override
  _GymChecklistPageState createState() => _GymChecklistPageState();
}

class _GymChecklistPageState extends State<GymChecklistPage> {
  final List<Map<String, dynamic>> _workouts = [
    {'name': 'Squats', 'done': false},
    {'name': 'Deadlifts', 'done': false},
    {'name': 'Bench Press', 'done': false},
    {'name': 'Pull-ups', 'done': false},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Gym Checklist')),
      body: ListView.builder(
        itemCount: _workouts.length,
        itemBuilder: (context, index) {
          return CheckboxListTile(
            title: Text(_workouts[index]['name']),
            value: _workouts[index]['done'],
            onChanged: (bool? value) {
              setState(() {
                _workouts[index]['done'] = value!;
              });
            },
          );
        },
      ),
    );
  }
}
