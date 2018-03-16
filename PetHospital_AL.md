### PetHospital API list ###
--n-- : nodejs
--p-- : python

* 登录 LOGIN
  ```
    /api/login {
      n to p:
        'username': 'XXX',
        'password': 'XXX'
      p to n:
        'success': 'TRUE' //登录成功
        'success': 'FALSE' //登录失败,不用标明原因
    }
  ```

* 职能学习模块 DutyLearning

  * 病例学习模块:
    ```
      /api/deseases {
        p to n:
          'deseases': [                                          //多个疾病大类序列
            {
              'id': 'jekjkcksllle',                              //根据后台机制定义的id,例如00000001
              'name': '炎症',                                    //疾病大类
              'series': [                                        //该疾病大类下的病种序列
                {'id': '000001', 'name': '口炎'},                //每个病种需要有id和name
                {'id': '000002', 'name': '肠道炎'},
                {'id': '000003', 'name': '妇科疾病'},
                {'id': '000004', 'name': '肛门炎'},
                {'id': '000005', 'name': '前列腺炎'},
                {'id': '000006', 'name': '男子医院特殊炎'},
                {'id': '000007', 'name': '乳腺炎'},
                {'id': '000008', 'name': '肚脐炎'},
                {'id': '000009', 'name': '口腔溃炎'},
                {'id': '000010', 'name': '胸肌炎'}
              ]
            },
            {
              'id': 'hellommotherfucker',
              'name': '癌症',
              'series': [
                {'seriesName': '癌症'},
                {'id': '000011', 'name': '口癌'},
                {'id': '000012', 'name': '肠道癌'},
                {'id': '000013', 'name': '妇科疾病'},
                {'id': '000014', 'name': '肛门癌'},
                {'id': '000015', 'name': '前列腺癌'},
                {'id': '000016', 'name': '男子医院特殊癌'},
                {'id': '000017', 'name': '乳腺癌'},
                {'id': '000018', 'name': '肚脐癌'},
                {'id': '000019', 'name': '口腔溃癌'},
                {'id': '000020', 'name': '胸肌癌'}
              ]
            }
          ]
      }

      /api/deseasecases/:id {                   //id为对应病种的id,例如上面示例中的口癌的id 000011
        p to n 
          'deseaseCases': [    //返回对应病种的病例序列,每个病例都包含id和名字
            {
              'id': 'jekjckwlwpckke11',
              'name': '郑光煜可怜的小狗狗得了前列腺炎'
            },
            {
              'id': 'jekjl2223wpckke1ekje11',
              'name': '王俊杰的小乌龟头炸了'
            }
          ]
      }

      /api/deseasecase/detail/:id { //id为上面返回的特定病种中的特定病例的id,例如上面的'name': '王俊杰的小乌龟头炸了'的id jekjl2223wpckke1ekje11
        p to n
          'deseaseCase': {
            'id': 'jekjl2223wpckke1ekje11',
            'name': '王俊杰的小乌龟头炸了',
            'description': '王俊杰在写代码, 二郎腿翘了太久了, 把自己养的小乌龟头挤炸了',
            'time': '上午9点',
            'picture': {              //如果没有图片,返回'picture': 'NONE'(大写注意)
              'urls': [
                {'url': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=534386446,2383379323&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3269230542,2079728320&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3351311726,1166292474&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1258893326,3098157884&fm=27&gp=0.jpg'}
              ]
            },
            'video': {       //如果没有视频,返回'video': 'NONE'(大写注意)
              'urls': [
                {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'},
                {'url': 'http://www.html5videoplayer.net/videos/toystory.mp4'}
              ]
            }
          }
      }
    ```
  
  * 角色扮演模块:
    ```
      /api/roles {
        p to n 
          'roles': [ //返回角色列表,每个角色包含id,name和des
            {'id': '000001', 'name': '狗狗鸡儿的小天使', 'description': '帮狗狗换尿布'},
            {'id': '000002', 'name': 'ROLE2', 'description': 'this is role 2'},
            {'id': '000003', 'name': 'ROLE3', 'description': 'this is role 3'}
          ]
      }

      /api/role/:id { //返回具体的角色的详细信息,不同于deseasecase,是一次性返回注意してくださいね,此处的:id就是是上方'roles'中的角色的具体id,例如'name': '狗狗鸡儿的小天使'这个角色的id就是000001
        p to n        //返回的数据不同于deseasecase是需要deseasecase字段包裹全部信息的,注意してくださいね、ダーリン～
          'name': '换尿布',
          'description': '帮狗狗换尿布',
          'details': [ //每个detail代表的可以是一个步骤,也可以是一个注意事项,后期可能会加上步骤和注意事项的区分字段,现在就先定义所有步骤靠前放,有注意事项的话集中起来,放在最后作为一个对象
            {
              'id': '000001',
              'name': '筋脉注射',
              'imgUrls': [
                {'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491201&di=4033099fdf0035ddd698a1774a8e2315&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2F7d3988de8b469e567b8253680afc99d028ad2b0e.jpg'},
                {'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491200&di=c43028d180e7797c068faab9675e9ab4&imgtype=0&src=http%3A%2F%2Fww1.sinaimg.cn%2Flarge%2Fc5a9b5efjw1e673b3mofkj20go0d6my7.jpg'},
                {
                  'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491200&di=3a2a1e0f8d6383e333389642a39f244e&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fw%3D580%2Fsign%3Df401aa2cc2ef76093c0b99971edca301%2Fb46f0223dd54564e6aad4a88bade9c82d0584f77.jpg'
                }
              ],
              'words': [
                {'word': 'you are the most beautiful girl in this world'},
                {'word': 'you are the most handsome boy in this fucking deep dark fantacy dormitory, leather man'}
              ],
              'videoUrls': [
                {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'},
                {'url': 'http://www.html5videoplayer.net/videos/toystory.mp4'}
              ]
            },
            {
              'id': '000002',
              'name': '搞比利',
              'imgUrls': [ //同,没有的话用'NONE'
                {'url': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=534386446,2383379323&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3269230542,2079728320&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3351311726,1166292474&fm=27&gp=0.jpg'},
                {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1258893326,3098157884&fm=27&gp=0.jpg'}
              ],
              'words': [ //同,没有的话用'NONE'
                {'word': 'you may want to go to the leather man\'s block'},
                {'word': 'oh fuck you leather man, you may want to fullfill my fantacies, come on, let\'s do this'}
              ],
              'videoUrls': [ //同,没有的话用'NONE'
                {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'}
              ]
            }
          ]
      }
    ```

* 医院导览展示 (尚未确定展示方式,暂时搁置)
  ```
    返回模型: --n--
      宠物医院基本结构模型, 前台区、档案室、门诊室、免疫室、化验室、治疗室、影像学检查室、药房、输液室、手术准备室、手术室、住院部、病理剖检室
    
    返回具体科室信息: --p--
      api1:
      /api/intro/:depatermentName
      1个科室对应多个信息api,每个信息api对应一次数据库查找
      e.g. 返回手术室的消毒流程,返回手术无菌要求,返回常规手术,反悔特殊手段,就有4个api
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
  
  api5:
  post请求：
  返回用户答题结果 记录
  /api/test/result
  {userID:,
   score:
   testType:
   testId:
  }
```
