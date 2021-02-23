<template>
  <v-card
    class="mx-auto"
    max-width="344"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">
          TODO
        </div>
        <v-list-item-title class="headline mb-1 text-justify text-wrap">
          死ぬまでに<br>
          やりたいこと<br>
          リスト
        </v-list-item-title>
        <v-list-item-subtitle class="mt-3">List of things to do before you die</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        size="150"
        
      >
      <img src="../../img/白黒、四角、工業、ロゴ.png" alt="死ぬまでにやりたいことリスト">
      </v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn
        class="ma-2"
        :loading="loading"
        :disabled="loading"
        color="secondary"
        outlined
        rounded
        text
        @click="googleLogin"
      >
        Googleへログイン
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<style>
</style>
<script>
import firebase from 'firebase'
import router from '../router'

export default {
  methods: {
    googleLogin: function() {
      const provider = new firebase.auth.GoogleAuthProvider()
      firebase.auth().signInWithPopup(provider).then(function() {
        router.push("/");
      }).catch(function(error) {
        alert(error.message)
      });
    }
  }
}
</script>