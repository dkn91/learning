package com.d_pak.dkn91.simplemath;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.d_pak.dkn91.starwarsmath.R;
import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.common.api.GoogleApiClient;

public class MainActivity extends AppCompatActivity {

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
    }

    public void displayresult(View v) {
        EditText mastersnametext = (EditText) findViewById(R.id.num1val);
        EditText aprenticesnametext = (EditText) findViewById(R.id.num2val);
        Integer n1 = Integer.parseInt(mastersnametext.getText().toString()), n2 = Integer.parseInt(aprenticesnametext.getText().toString());
        Integer ans = n1 + n2;
        TextView result = (TextView) findViewById(R.id.answer);
        result.setText("Answer: " + ans.toString());
    }

    public void displaysubtractresult(View v) {
        EditText mastersnametext = (EditText) findViewById(R.id.num1val);
        EditText aprenticesnametext = (EditText) findViewById(R.id.num2val);
        Integer n1 = Integer.parseInt(mastersnametext.getText().toString()), n2 = Integer.parseInt(aprenticesnametext.getText().toString());
        Integer ans = n1 - n2;
        TextView result = (TextView) findViewById(R.id.answer);
        result.setText("Answer: " + ans.toString());
    }

    @Override
    public void onStart() {
        super.onStart();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Main Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://com.d_pak.dkn91.simplemath/http/host/path")
        );
        AppIndex.AppIndexApi.start(client, viewAction);
    }

    @Override
    public void onStop() {
        super.onStop();

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        Action viewAction = Action.newAction(
                Action.TYPE_VIEW, // TODO: choose an action type.
                "Main Page", // TODO: Define a title for the content shown.
                // TODO: If you have web page content that matches this app activity's content,
                // make sure this auto-generated web page URL is correct.
                // Otherwise, set the URL to null.
                Uri.parse("http://host/path"),
                // TODO: Make sure this auto-generated app deep link URI is correct.
                Uri.parse("android-app://com.d_pak.dkn91.simplemath/http/host/path")
        );
        AppIndex.AppIndexApi.end(client, viewAction);
        client.disconnect();
    }
}
