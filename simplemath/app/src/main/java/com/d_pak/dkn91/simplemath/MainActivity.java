package com.d_pak.dkn91.simplemath;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void displayresult(View v){
        EditText mastersnametext=(EditText)findViewById(R.id.num1val);
        EditText aprenticesnametext=(EditText)findViewById(R.id.num2val);
        Integer n1= Integer.parseInt(mastersnametext.getText().toString()), n2= Integer.parseInt(aprenticesnametext.getText().toString());
        Integer ans=n1+n2;
        TextView result = (TextView)findViewById(R.id.answer);
        result.setText("Answer: " + ans.toString());
    }
}
