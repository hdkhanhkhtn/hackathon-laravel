<?php

namespace App\Http\Controllers;

use App\User;
use App\Article;
use Illuminate\Http\Request;
use App\Http\Requests;
use JWTAuth;
use Response;
use App\Repositories\Transformers\ArticleTransformer;
use \Illuminate\Http\Response as Res;
use Validator;
use Tymon\JWTAuth\Exceptions\JWTException;
use Illuminate\Support\Facades\Input;

class ArticleController extends ApiController
{

    /**
     * @var \App\Repository\Transformers\ArticleTransformer
     * */
    protected $articleTransformer;


    public function __construct(ArticleTransformer $articleTransformer)
    {

        $this->articleTransformer = $articleTransformer;

    }

    /**
     * Get all articles
     * @author: HDK
     * @param: none
     * @return: Json String response
     */
    public function index(){

        $api_token = Input::get('api_token');

        try{

            $user = JWTAuth::toUser($api_token);

            $limit = Input::get('limit') ?: 3;

            $articles = Article::paginate($limit);
            
            return $this->respondWithPagination($articles, [
                'articles' => $this->articleTransformer->transformCollection($articles->all())
            ], 'Records Found!');

        }catch(JWTException $e){

            return $this->respondInternalError("An error occurred while performing an action!");

        }
        
    }
}
