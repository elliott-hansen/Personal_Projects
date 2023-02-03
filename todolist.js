// ToDoList - - Elliott Hansen (11/08/22)
// I found it sort of difficult to add a lot of comments throughout this project since the method names make them pretty redundant.
// I do provide an introduction upon an initial run that provides information as well, which I believe would be useful.

// Task class, holds all of the details about each task and has methods for altering them.
class Task {
  constructor(name, desc, due = 0) {
    this.prior = 0;
    this._name = name;
    // Date created cannot be changed, obviously.
    this._date = new Date().toLocaleDateString();
    this._desc = desc;
    this._status = 'In Progress...';
    if(due === 0) {
      this._due = this._date
    }
    else {
      this._due = due;
    }
  }
  get duedate() {
    return this._due;
  }
  get date() {
     return this._date;
  }
  get priority() {
     return this.prior;
  }
  get status() {
    return this._status;
  }
  get desc() {
    return this._desc;
  }
  get name() {
    return this._name;
  }
  updateName(name = '') {
    console.log(' - Renaming task #'+this.priority+'...');
    if(name === '') {
      this._name = prompt(' - Enter a new name for\''+this._name+'\'');
    }
    else {
      this._name = name;
    }
    console.log(' - Renamed task #'+this.priority+' to \''+this._name+'\'!');
  }
  updateDescription(desc = '') {
    console.log(' - Redescribing task #'+this.priority+'...');
    if(desc === '') {
      this._desc = prompt(' - Enter a new description for \''+this._name+'\'');
    }
    else {
      this._desc = desc;
    }
    console.log(' - Redescribed \''+this._name+'\'!');
  }
  updateStatus(inp = 0) {
    console.log(' - Updating status of task #'+this.priority+'...');
    if((inp >= 0) && (inp < 3)) {
      this._status = ['In Progress...', 'Working On...', 'Finished! (Date: '+new Date().toLocaleDateString()+')'][inp];
      }
    else {
      console.log(' - Please enter 0, 1, or 2 to set the following status:\n- 0:  In Progress...\n- 1:  Working On...\n- 2:  Finished! (Date: ---)');
    }
  }
  updateDueDate(due = '') {
    console.log(' - Changing due date for task #'+this.priority+'...');
    if(due === '') {
      this._due = prompt(' - Enter a new due date for for \''+this._name+'\'');
    }
    else {
      this._due = due;
    }
    console.log(' - Changed due date for \''+this._name+'\'!');
    }
  showInfo(){
    console.log('\t'+'='.repeat(100));
    console.log(' - '+this.priority+')   NAME: '+this.name+' | CREATED: '+this.date+' | STATUS: '+this.status+' | DUE: '+this.duedate);
    console.log('\t'+'='.repeat(100));
    console.log('\tDESC: '+this.desc.replace(/.{100}/g, '$&\n\t'));
  }
}
// ToDoList class, creates an array to hold tasks and has methods to interact with them.
class ToDoList {
  constructor() {
    const arr = [];
    this.contents = arr;
  }
  selectItem(index) {
    if(index >= 0 && index < this.contents.length) {
    return this.contents[index];
    }
    else {
      console.log(' - A valid input was not provided: index out of range.');
    }
  }
  _updatePriorities() {
    for(let i = 0; i < this.contents.length; i++) {
      this.contents[i].prior = i;
    }
  }
  setPosition(original, updated) {
    if((original >= 0 && original < this.contents.length) && (updated >= 0)) {
      if(updated >= this.contents.length) {
        updated = this.contents.length-1;
      }
    let temp = this.contents[original];
    this.contents.splice(original, 1);
    this.contents.splice(updated, 0, temp);
    this._updatePriorities();
    console.log(' - Moved item at index '+original+' to '+updated);
    }
  }
  addItem(item) {
    if(typeof item != 'object') {
      console.log('A valid input was not provided: must be of type \'object\'');
    }
    this.contents.push(item);
    this._updatePriorities();
    console.log(' - Added item');
  }
  removeItem(index) {
    if(index >= 0 && index < this.contents.length) {
    this.contents.splice(index,1);
    this._updatePriorities();
    console.log(' - Removed item');
    }
    else {
      console.log('A valid input was not provided: index out of range.');
    }
  }
  showContents() {
    console.log(' - Displaying contents...');
    for(let i = 0; i < this.contents.length; i++) {
      this.contents[i].showInfo();
      console.log('');
    }
  }
}

let tdl = new ToDoList();
tdl.addItem(new Task('Buy groceries','Run to supermarket and grab groceries for tonight. Needed: eggs, milk, onions, basil, ground beef, oranges, wine.'));
tdl.addItem(new Task('Take Toby to soccer practice', 'Toby is playing his school\'s rival at 5:30 PM on Friday'));
tdl.addItem(new Task('Prepare for anniversary', 'Genevieve isn\'t expecting me to go all out this time around, but I want to do something big for her. (European vacation??)'));
tdl.selectItem(0).updateStatus(2);
tdl.selectItem(1).updateDueDate('11/11/22');
tdl.selectItem(2).updateDueDate('04/13/23');
tdl.addItem(new Task('URGENT: Pick up perscription','Mom has three tablets remaining and will be out by tomorrow, I need to swing by the pharmacy TODAY!'));
tdl.setPosition(3,0);
console.log('\n'+'/ '.repeat(30)+'ToDoList '+'/ '.repeat(30)+'\n\nThis is a fun example of a to-do-list made with my implementation. Provided already are some tasks who may have had their due date, position in the list, status, etc. altered by some of the commands. To play around with it yourself, try utilizing some of the commands listed below (the name of the pre-made ToDoList object is \'tdl\'):'.replace(/.{125}/g, '$&\n'));
console.log('\n - tdl.showContents(): Displays all of the contents of the list, formatted like the example below.\n - tdl.addItem(object): Adds a new item into the ToDoList. Only accepts object datatype as a parameter.\n - tdl.removeItem(index): Removes the object in the list at the provided index.\n - tdl.setPosition(index1, index2): Moves the object at index1 to index2 in the list.\n - tdl.selectItem(index): \'Select\' the indexed item to alter using Task methods, listed below. (Example usage: tdl.selecItem(3).showInfo())');
console.log('\n - task.updateName(): Updates the name of the task selected. Will accept a string parameter, or will prompt the user for input.\n - task.updateDescription(): Updates the description of the task selected. Will accept a string parameter, or will prompt the user for input.\n - task.updateStatus(0-2): Updates the status of the selected task to one of the following:\n\t- 0:  In Progress...\n\t- 1:  Working On...\n\t- 2:  Finished! (Date: ---)\n - task.updateDueDate(string): Updates the due date of the selected task to a string input.\n - task.showInfo(): Displays the formatted details of the current selected task.');
console.log('\n'+'/ '.repeat(65)+'\n');
tdl.showContents();