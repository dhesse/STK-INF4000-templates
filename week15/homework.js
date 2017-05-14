window.onload = function() {
    // 1. Write a function to set the innerHTML of an object
    //    to a given value.
    var setInnerHTML = function(id, newValue) {
	var elem = document.getElementById(id);
	elem.innerHTML = newValue;
    }
    // 2. Write a reduce function for Javascript arrays, in analog ot Python's reduce.
    //    It should produce e.g.
    //      reduce([1, 2, 3], function(x, y) { return x + y; }, 0) === 1 + 2 + 3;
    var reduce = function(array, fn, nullvalue) {
	var i, result = nullvalue;
	for (i = 0; i < array.length; i += 1)
	    result = fn(result, array[i])
	return result;
    }
    // 2. Write a function to add a reduce method to the Array prototype. After calling
    //    the function, one should be able to get
    //       [1,2,3].my_reduce(function(x, y) { return x * y; }, 1) === 1 * 2 * 3;
    var addReducePrototype = function() {
	Array.prototype.my_reduce = function(fn, nullval) {
	    return reduce(this, fn, nullval);
	};
    }

    var checks = [
	{task: 'Task 1',
	 check: function() {
	     setInnerHTML('task_1_div', 'Good Job!');
	     if (document.getElementById('task_1_div').innerHTML === 'Good Job!')
		 return 'PASS';
	     else
		 return 'FAIL';
	 },
	},
	{task: 'Task 2',
	 check: function() {
	     if (reduce([1, 2, 3], function(x, y) { return x + y; }, 0) === 1 + 2 + 3)
		 return 'PASS';
	     else
		 return 'FAIL';
	 },
	},
	{task: 'Task 3',
	 check: function() {
	     addReducePrototype();
	     try {
		 if ([1,2,3].my_reduce(function(x, y) { return x * y; }, 1) === 1 * 2 * 3)
		     return 'PASS';
		 else
		     return 'FAIL';
	     } catch(e) {
		 return 'FAIL';
	     }
	 },
	}

    ];

    var apply_check = function(check) {
	var check_list = document.getElementById('check_list');
	var li = document.createElement('li');
	li.innerHTML = check.task + ": " + check.check();
	check_list.appendChild(li);
    }

    for (var i = 0; i < checks.length; i += 1)
	apply_check(checks[i]);
}
