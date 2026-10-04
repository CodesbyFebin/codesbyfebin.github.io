document.documentElement.classList.add('js');
const themeButton = document.querySelector('[data-theme-toggle]');
function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  if (themeButton) { themeButton.textContent = theme === 'dark' ? 'Light' : 'Dark'; themeButton.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`); }
}
let savedTheme = 'dark';
try { savedTheme = localStorage.getItem('portfolio-theme') || 'dark'; } catch {}
setTheme(savedTheme === 'light' ? 'light' : 'dark');
themeButton?.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  setTheme(theme); try { localStorage.setItem('portfolio-theme', theme); } catch {}
});
const menu = document.querySelector('[data-menu]');
const navigation = document.querySelector('#navigation');
menu?.addEventListener('click', () => { const open = navigation?.classList.toggle('open'); menu.setAttribute('aria-expanded', String(Boolean(open))); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && navigation?.classList.contains('open')) { navigation.classList.remove('open'); menu?.setAttribute('aria-expanded', 'false'); menu?.focus(); } });
const projectGrid = document.querySelector('[data-project-grid]');
if (projectGrid) {
  const cards = Array.from(projectGrid.querySelectorAll('[data-project]'));
  const search = document.querySelector('#project-search');
  const category = document.querySelector('#project-category');
  const status = document.querySelector('#project-status');
  const sort = document.querySelector('#project-sort');
  function updateProjects() {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    cards.forEach(card => {
      const match = card.dataset.search.includes(query) && (category.value === 'all' || card.dataset.category === category.value) && (status.value === 'all' || card.dataset.status === status.value);
      card.hidden = !match; if (match) count++;
    });
    const ordered = [...cards].sort((a, b) => sort.value === 'stars' ? Number(b.dataset.stars) - Number(a.dataset.stars) || a.dataset.name.localeCompare(b.dataset.name) : sort.value === 'updated' ? b.dataset.updated.localeCompare(a.dataset.updated) : a.dataset.name.localeCompare(b.dataset.name));
    ordered.forEach(card => projectGrid.appendChild(card));
    document.querySelector('[data-result-count]').textContent = `${count} of ${cards.length} repositories · snapshot 3 October 2026`;
    document.querySelector('[data-no-results]').hidden = count !== 0;
  }
  [search, category, status, sort].forEach(control => control.addEventListener(control === search ? 'input' : 'change', updateProjects));
  document.querySelector('[data-reset]')?.addEventListener('click', () => { search.value=''; category.value='all'; status.value='all'; sort.value='name'; updateProjects(); search.focus(); });
  updateProjects();
}
const briefForm = document.querySelector('[data-brief-form]');
if (briefForm) {
  const output = document.querySelector('[data-brief-output]');
  const copy = document.querySelector('[data-copy-brief]');
  briefForm.addEventListener('submit', event => {
    event.preventDefault();
    const data = new FormData(briefForm);
    output.textContent = `Collaboration brief\n\nName: ${data.get('name')}\nTopic: ${data.get('topic')}\nProject/source: ${data.get('source') || 'To discuss'}\n\nCurrent situation and desired result:\n${data.get('message')}\n\nConstraints and acceptance evidence:\n${data.get('constraints') || 'To agree'}`;
    copy.disabled = false;
    document.querySelector('[data-brief-status]').textContent = 'Brief created locally. Copy it to your chosen contact channel.';
  });
  copy.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(output.textContent); document.querySelector('[data-brief-status]').textContent = 'Copied. No message has been sent.'; }
    catch { const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(output); selection.removeAllRanges(); selection.addRange(range); document.querySelector('[data-brief-status]').textContent = 'Select and copy the highlighted brief using your device’s copy action.'; }
  });
}
