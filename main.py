import gradio as gr
import tensorflow as tf
import settings
from models import my_densenet
import matplotlib as mpl
mpl.use('TkAgg')


# 导入模型
model = my_densenet()
# 加载训练好的参数
model.load_weights(settings.MODEL_PATH)


def classify_pet_image(input_image):
    """
    宠物图片分类接口，上传一张图片，返回此图片上的宠物是哪种类别，概率多少
    """
    # 进行数据预处理
    # x = tf.image.decode_image(input_image, channels=3)
    x = tf.convert_to_tensor(input_image)
    x = tf.image.resize(x, (224, 224))
    x = x / 255.
    x = (x - tf.constant(settings.IMAGE_MEAN)) / tf.constant(settings.IMAGE_STD)
    x = tf.reshape(x, (1, 224, 224, 3))
    # 预测
    y_pred = model(x)
    pet_cls_code = tf.argmax(y_pred, axis=1).numpy()[0]
    pet_cls_prob = float(y_pred.numpy()[0][pet_cls_code])
    pet_cls_prob = '{}%'.format(int(pet_cls_prob * 100))
    pet_class = settings.CODE_CLASS_MAP.get(pet_cls_code)
    # 格式化输出为纯文本
    output_text = "宠物类别：{}  \n概率：{}".format(pet_class, pet_cls_prob)

    return output_text


gr.close_all()
demo = gr.Interface(fn=classify_pet_image,
          inputs=[gr.Image(label="Upload image")],
          outputs=[gr.Textbox(label="识别结果")],
          title="宠物识别Demo",
          description="Classify your pet!",
          allow_flagging="never"
                   )

demo.launch(share=True, debug=True, server_port=10055)
