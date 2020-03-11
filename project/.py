history = request.session.get('history', [])
for item in history:
    self.children.append(MenuItem(
        title=item['title'],
        url=item['url']
    ))
history.insert(0, {
    'title': context['title'],
    'url': request.META['PATH_INFO']
})
if len(history) > 5:
    history = history[:5]
request.session['history'] = history