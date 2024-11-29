import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class GetOTP extends StatelessWidget {
  const GetOTP({super.key});

  @override
  Widget build(BuildContext context) {
    return Material( 
      child: Form(
        child: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
          SizedBox(
            height: 68,width: 64,
            child: TextFormField(
              onChanged: (value) {
                if(value.length == 1) {
                  FocusScope.of(context).nextFocus();
                }
              },
              onSaved: (pin1){},
              decoration: InputDecoration(hintText:"0"),
              style: Theme.of(context).textTheme.titleLarge,
              keyboardType: TextInputType.number,
              inputFormatters: [
                LengthLimitingTextInputFormatter(1),
                FilteringTextInputFormatter.digitsOnly
              ],
            ),
            
          ),
           SizedBox(
            height: 68,width: 64,
            child: TextFormField(
              onChanged: (value) {
                if(value.length == 1) {
                  FocusScope.of(context).nextFocus();
                }
              },
              onSaved: (pin2){},
              decoration: InputDecoration(hintText:"0"),
              style: Theme.of(context).textTheme.titleLarge,
              keyboardType: TextInputType.number,
              inputFormatters: [
                LengthLimitingTextInputFormatter(1),
                FilteringTextInputFormatter.digitsOnly
              ],
            ),
            
          ),
           SizedBox(
            height: 68,width: 64,
            child: TextFormField(
              onChanged: (value) {
                if(value.length == 1) {
                  FocusScope.of(context).nextFocus();
                }
              },
              onSaved: (pin3){},
              decoration: InputDecoration(hintText:"0"),
              style: Theme.of(context).textTheme.titleLarge,
              keyboardType: TextInputType.number,
              inputFormatters: [
                LengthLimitingTextInputFormatter(1),
                FilteringTextInputFormatter.digitsOnly
              ],
            ),
            
          ),
           SizedBox(
            height: 68,width: 64,
            child: TextFormField(
              onChanged: (value) {
                if(value.length == 1) {
                  FocusScope.of(context).nextFocus();
                }
              },
              onSaved: (pin4){},
              decoration: InputDecoration(hintText:"0"),
              style: Theme.of(context).textTheme.titleLarge,
              keyboardType: TextInputType.number,
              inputFormatters: [
                LengthLimitingTextInputFormatter(1),
                FilteringTextInputFormatter.digitsOnly
              ],
            ),
            
          ),
          
              ],),
        ),
      ),);
  }
}
