import 'package:flutter/material.dart';
import 'package:pickupexpress/screens/get_otp.dart';
import 'package:pickupexpress/screens/home_screen.dart';
import 'package:pickupexpress/screens/login_screen.dart';
import 'package:pickupexpress/screens/signup_screen.dart';



void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
    home: const LoginScreen()
    );
  }
}
