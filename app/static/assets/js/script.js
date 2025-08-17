function addEventToClasses(selector, event_type, event_handler) {
  const elements = document.querySelectorAll(selector);
  for (const element of elements) {
    const id = element.dataset.id;
    element.addEventListener(event_type, (e) => {
      e.preventDefault();
      event_handler(id);
    });
  }
}

async function markDoneTodo(todo_id) {
  try {
    const response = await fetch(`/${todo_id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        is_done: true,
      }),
    });

    const response_json = await response.json();
    console.log('Response JSON:', response_json);

    if (response.ok && response_json.success) {
      window.location.replace('/');
      console.log(`Todo ID #${todo_id} has been updated!`);
    } else {
      console.error(`Failed to update TODO ID #${todo_id}`);
    }
  } catch (err) {
    console.error(err);
  }
}

async function updateTodo(todo_id) {
  try {
    const todo_text = document.querySelector('#todo-text');
    if (!todo_text) return;

    const response = await fetch(`/${todo_id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: todo_text.value,
      }),
    });

    const response_json = await response.json();
    console.log('Response JSON:', response_json);

    if (response.ok && response_json.success) {
      window.location.replace('/');
      console.log(`Todo ID #${todo_id} has been updated!`);
    } else {
      console.error(`Failed to update TODO ID #${todo_id}`);
    }
  } catch (err) {
    console.error(err);
  }
}

async function deleteTodo(todo_id) {
  try {
    const response = await fetch(`/${todo_id}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ t: 't' }),
    });

    const response_json = await response.json();
    console.log('Response JSON:', response_json);

    if (response.ok && response_json.success) {
      window.location.reload();
      console.log(`Todo ID #${todo_id} has been deleted!`);
    }
  } catch (err) {
    console.error(err);
  }
}

addEventToClasses('.btn-mark-as-done', 'click', markDoneTodo);
addEventToClasses('.btn-update', 'click', updateTodo);
addEventToClasses(".btn-delete input[type='submit']", 'click', deleteTodo);
