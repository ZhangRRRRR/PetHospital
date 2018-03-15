<template>
  <div>
      <ul>
        <li v-for="desease in deseasesData.deseases" :key="desease.id">
          <p>{{desease.name}}</p>
          <ul>
            <li v-for="series in desease.series" :key="series.id">
              <router-link :to="'/deseaseseries/' + series.id">
                <p>{{series.name}}</p>
              </router-link>
            </li>
          </ul>
        </li>
      </ul>
      <button v-on:click="logOut()">登出</button>
      <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
      <button v-on:click="jumpToPage('DutyLearningPage')">回到职能学习页面</button>
  </div>
</template>

<script>
import PHHeader from '../../components/PHHeader.vue'
import PHFooter from '../../components/PHFooter.vue'
export default {
  components: { PHHeader, PHFooter },
  data () {
    return {
      deseasesData: {
        'deseases': [
          {
            'id': 'jekjkcksllle',
            'name': '炎症',
            'series': [
              {'id': '000001', 'name': '口炎'},
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
    }
  },
  created () {
    this.checkLogin()
  },
  methods: {
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
        // do nothing
      } else {
        this.login()
      }
    },
    login () {
      this.$router.push({
        name: 'LoginPage',
        params: {
          jumpFromPage: 'WelcomePage'
        }
      })
    },
    jumpToPage (pageName) {
      this.$router.push({
        name: pageName
      })
    },
    logOut () {
      this.$api.setLoginStatus('LOGOUT')
      this.jumpToPage('LoginPage')
    }
  }
}
</script>
