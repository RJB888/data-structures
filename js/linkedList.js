'use strict'

class Node{

  constructor(val){
    this.value = val
    this.next = null
  }
}

class LinkedList{

  constructor(){
    this.head = null
    this.size = 0
  }

  push(val){
    let newNode = new Node(val)
    newNode.next = this.head
    this.head = newNode
    this.size ++

  }

  pop(){
    if(this.head === null){
      return 'List is empty'
    }
    else{
      let temp = this.head.value
      this.head = this.head.next
      this.size --
      return temp
    }

  }

  size(){
    return this.size
  }

  search(val){
    let tempNode = this.head
    if (this.head === null){
      return 'List is empty.'
    }
    try{
      while(tempNode !== null){
        if (tempNode.val === val){
          return tempNode
        }
        else{
          tempNode = tempNode.next
        }
      }
    }
    catch(e){
      return 'Node not found.'
    }
  }

  remove(val){
    let curr = this.head
    while (curr !== null ){
      if (curr.next === val){
        curr.next = curr.next.next
        this.size --
        return
      }
      curr = curr.next
    }
  }

  display(){
    let cur = this.head
    let output = []
    while (cur !== null ){
      output.append(cur.val)
      cur = cur.next
    }
    return output.join(', ')
  }

}

module.exports = {LinkedList}
