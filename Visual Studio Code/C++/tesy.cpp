In the C++ Toolkit for Qt (CTK), you can set a font to be extra bold by specifying the weight of the font in your code. Here's an example of how you might do this using Qt:

```cpp
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QFont>

int main(int argc, char *argv[]) {
        QApplication app(argc, argv);

            QWidget window;
                QLabel label(&window);
                    label.setText("Extra Bold Text");

                        QFont font = label.font();
                            font.setWeight(QFont::ExtraBold); // Set font weight to ExtraBold
                                label.setFont(font);

                                    window.show();
                                        return app.exec();
                                        }
                                        ```

                                        In this code:

                                        1. `QFont::ExtraBold` is used to set the font weight to extra bold.
                                        2. The `label.setFont(font)` function applies the font to the label.

                                        Make sure you have the necessary Qt libraries linked to your project to compile and run this code.
}