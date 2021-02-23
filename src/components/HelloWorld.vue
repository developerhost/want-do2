<template>
  <div id="task">
    タスクページ
    <p>current user: {{ username }}</p>
    <p>current uid: {{ uid }}</p>

    <!-- New task -->
    <div>
      <v-layout wrap>
      <v-text-field
        v-model="newTodoName"
        solo
        placeholder="やりたいこと"
      ></v-text-field>
      <v-btn
        @click="createTodo()"
        class="mx-2"
        fab
        dark
        color="indigo"
      >
        <v-icon dark>
          mdi-plus
        </v-icon>
      </v-btn>
      </v-layout>
    </div>

    <!-- todo一覧表示 -->
<v-container>
  <v-col class="mb-5" cols="12">
    <v-row justify="center" v-for="(todo, key) in todos" :key="todo.id">
      <span>
          {{ todo.name }}
      </span>
      <span>

          <a 
          href="#" 
          dark
          v-if="todo.isComplete == true"
          @click="updateIsCompleteTodo(todo, key)"
          label="red"
          color="red"
           >
           </a>

           <a href="#"
           dark
           v-if="todo.isComplete == false"
           @click="updateIsCompleteTodo(todo, key)"
           label="indigo"
           color="indigo"
           >
           </a>
      </span>
      
    </v-row>
  </v-col>
</v-container>
  </div>
</template>

<style>
</style>

<script>
import firebase from 'firebase'

export default {
  name: "Task",
  data () {
    return {
      username: firebase.auth().currentUser.displayName,
      database: null,
      todosRef: null,
      todos: [],
      uid: firebase.auth().currentUser.uid,
    };
  },
  created: function(){
    this.database = firebase.database();
    this.uid = firebase.auth().currentUser.uid;
    this.todosRef = this.database.ref("todos/" + this.uid); //'/todos/<uid>/*' 以下を参照する

    //データに変更があるときに実行される
    var _this = this;
    this.todosRef.on("value", (snapshot) => {
      _this.todos = snapshot.val(); //再取得してtodosに格納する
    })
  },



  methods: {
    createTodo: function() {
      if(this.newTodoName == ""){
        return;
      }
      this.todosRef.push({
        name: this.newTodoName,
        isComplete: false
      });
      this.newTodoName = ""
    },

    // 完了・未完了の値の更新
    updateIsCompleteTodo: function(todo, key){
      if(todo.isComplete == true) {
        todo.isComplete = false;
      } else {
        todo.isComplete = true;
      }
      var updates = {};
      updates[key] = todo;
      this.todosRef.update(updates);
    }
  },
}
</script>