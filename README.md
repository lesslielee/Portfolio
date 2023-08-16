# Portfolio
To show some works I've done
## Train Those Lips (Flutter)
### Layout

Layout design - Flexible, Expanded to let the app fit in different screen sizes 

### Packages used in the project

[animated_text_kit](https://pub.dev/packages/animated_text_kit) <img src="https://pub.dev/static/hash-rp3lqslb/img/ff-banner-desktop-2x.png" width=20 /> -  to show animation effect of the text or notification

[percent_indicator](https://pub.dev/packages/percent_indicator) - to show progress with animation indicator

[shared_preferences](https://pub.dev/packages/shared_preferences) <img src="https://pub.dev/static/hash-rp3lqslb/img/ff-banner-desktop-2x.png" width=20 /> - to serialize the scores onto local mobile devices

[video_player](https://pub.dev/packages/video_player) - to playback the recorded video

[audioplayers](https://pub.dev/packages/audioplayers) - to play the notification sound

[intl](https://pub.dev/packages/intl) <img src="https://pub.dev/static/hash-rp3lqslb/img/ff-banner-desktop-2x.png" width=20 /> - to format the number with decimal format (e.g. 1,234,567) 

[uuid](https://pub.dev/packages/uuid) - to generate unique id 

[url_launcher](https://pub.dev/packages/url_launcher) <img src="https://pub.dev/static/hash-rp3lqslb/img/ff-banner-desktop-2x.png" width=20 /> - to browse webpage in the App

[dio](https://pub.dev/packages/dio) - to take the HTTP request (POST, GET, etc) to communicate between the App and backend server

### Tips & Skills & Technologies
- Use 3rd party Fonts (e.g. [**'Cristik'**](https://textfonts.net/cristik-a-creative-type.html)) in the project
- Timer(Duration()) and Timer.periodic(Duration())
  - ```Timer(Duration(microseconds: _delayDrawCircleTime), () { _startDrawCircle = true;});```
  - ```Timer.periodic(Duration(seconds: _Interval), (timer) async { await someAsyncCall(); };```
- TextStyle(shadows) and DefaultTextStyle()
- Icon nested in a container with BoxDecoration(using shape, color, boxShadow, etc.) to make a decorated button
- GestureDetector() to make a Picture or Icon reactive to the touch, tap, etc.
- HTTP header, request form, response data, and JSON encode/decode
- Flexible and Expanded could not be nested with each other, they should only be nested under the FLEX widget (e.g. Column, Row) (separately)
- Other flutter packages I have poked around
  - [animated_flip_counter](https://pub.dev/packages/animated_flip_counter)
  - [step_progress_indicator](https://pub.dev/packages/step_progress_indicator)
  - [just_audio](https://pub.dev/packages/just_audio) <img src="https://pub.dev/static/hash-rp3lqslb/img/ff-banner-desktop-2x.png" width=20 />
  
