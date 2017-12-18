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
    while(tempNode !== null){
      if (tempNode.value === val){
        return tempNode
      }
      else{
        tempNode = tempNode.next
      }
    }
    return 'Node not found.'
  }

  remove(val){
    let curr = this.head
    while (curr !== null ){
      if (curr.next.value === val){
        curr.next = curr.next.next
        this.size --
        return
      }
      curr = curr.next
    }
  }

  display(){
    if (this.head === null)
      return
    let cur = this.head
    let output = []
    while (cur !== null ){
      output.push(cur.value)
      cur = cur.next
    }
    return output.join(', ')
  }

}

module.exports = {LinkedList}
