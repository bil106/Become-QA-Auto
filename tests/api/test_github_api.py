import pytest



@pytest.mark.api
def test_user_exists(github_api):  
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):   
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r['items'][0]['name'] 

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist ')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('b')
    assert r['total_count'] != 0


@pytest.mark.api
def test_find_emojis(github_api):
    emojis= github_api.get_emojis()
    assert emojis['8ball'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f3b1.png?v8'
    assert emojis['abacus'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f9ee.png?v8'
    assert emojis['mexico'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f1f2-1f1fd.png?v8'
    assert emojis['zzz'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4a4.png?v8'
    assert emojis['+1'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8'
  
  

@pytest.mark.api
def test_valid_commit(github_api):
     owner = "octocat"
     repo = "Hello-World"
     ref = "6dcb09b5b57875f334f61aebed695e2e4193db5e" 
     commit = github_api.get_commits(owner,repo,ref)
     
     assert commit['message'] == 'No commit found for SHA: 6dcb09b5b57875f334f61aebed695e2e4193db5e'