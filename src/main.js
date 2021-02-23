import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import firebase from 'firebase'

Vue.config.productionTip = false

 // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyC_Wr1OVIKtvgsB-9naxxGkbP4jsMhPurk",
    authDomain: "want-do2.firebaseapp.com",
    databaseURL: "https://want-do2-default-rtdb.firebaseio.com",
    projectId: "want-do2",
    storageBucket: "want-do2.appspot.com",
    messagingSenderId: "994655369155",
    appId: "1:994655369155:web:fc95516d345df31d002f76",
    measurementId: "G-TPK7QR249N"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
