### PetHospital API list ###
--n-- : nodejs
--p-- : python


* 医院导览展示
```
  返回模型: --n--
    宠物医院基本结构模型, 前台区、档案室、门诊室、免疫室、化验室、治疗室、影像学检查室、药房、输液室、手术准备室、手术室、住院部、病理剖检室
  
  返回具体科室信息: --p--
    api1:
    /api/intro/:depatermentName
    1个科室对应多个信息api,每个信息api对应一次数据库查找
    e.g. 返回手术室的消毒流程,返回手术无菌要求,返回常规手术,反悔特殊手段,就有4个api
```

* 职能学习模块
```
  角色扮演模式无 --p-- 
  
  返回病例结构树: --p--
    api1:
    /api/disease
    e.g.内科病例包含若干病例,返回json格式或者xml格式,总之要有包含关系体现
  
    api2:
    /api/disease/:diseaseName
  返回某个病种的结构信息: --p--
    结构信息json格式数据
    文字直接返回明文
    图片返回url
    视频返回url

    e.g.{
      返回json如下:
      //没有就写NONE(string)
      胆囊炎{
        疾病名称:胆囊炎
        接诊:{
          文字:XXXXXXXXXX胆囊炎最高
          照片:http://XXXXXX.XXX.XX/IMG/fkejkfekjk
          视频:.....
        }
        病例检查:{
          文字:XXXXXXXXXX胆囊炎最高
          照片:http://XXXXXX.XXX.XX/IMG/fkejkfekjk
          视频:.....
        }
        诊断结果:{
          文字:XXXXXXXXXX胆囊炎最高
          照片:NONE
          视频:.....
        }
        治疗方案:{
          文字:XXXXXXXXXX胆囊炎最高
          照片:http://XXXXXX.XXX.XX/IMG/fkejkfekjk
          视频:.....
        }
      }
    }
```
* 测试
```
  api1:
  get请求某一项目的试题 从id开始
  /api/test/:class/:id?
  
  api2:
  get请求所有存在的考试
  /api/test/
  
  api3:
  get请求某一考试全部试题
  /api/test/:id
  
  api4:
  get请求生成自我测试 并返回全部试题内容。
  /api/test/self 
  
```
