  #-*-coding=utf-8 -*-
  import qrcode
  import time
  import os
  import ConfigParser
  #获取最新构建的数据包
  class Qr_config():
      def __init__(self):
          self.cf = ConfigParser.ConfigParser()
         self.cf.read("config.properties")
         self.jenkins_pro_address = self.cf.get("config", "jenkins_address")
         self.project_name = self.cf.get("config", "project_name")
         self.apk_home = self.cf.get("config", "apk_home")
         self.jenkins_space = self.cf.get("config", "jenkins_space")
         self.today_time = time.strftime("%Y-%m-%d")
 
     def get_apk_url(self):
 
         today_dir = "%s\\jobs\\%s\\workspace\\%s\\%s" % (self.jenkins_space,
                                                    self.project_name,
                                                    self.apk_home,
                                                    self.today_time)
         if os.path.exists(today_dir):
             file_list = os.listdir(today_dir)
             file_name = file_list[-1]
             if file_name:
                 down_url = "%s/job/%s/ws/%s/%s/%s" % (self.jenkins_pro_address,
                                             self.project_name,
                                             self.apk_home,
                                             self.today_time,
                                             file_name)
                 return down_url
             else:
                 print "文件不存在，今日构建失败！"
         else:
             print "今日不存在构建！"
 
 if __name__ == "__main__":
     link = Qr_config().get_apk_url()
     png = "C:\Users\\Administrator\\Desktop\\1.3.2top.png"
     qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=8,
                        border=8,)
     qr.add_data(link)
     qr.make(fit=True)
     img = qr.make_image()
     img.save("android_qr_code.png", '')
